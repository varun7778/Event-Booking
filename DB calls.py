#procedure checks if logistics are avaiable adds to logtable
CREATE DEFINER=`root`@`localhost` PROCEDURE `p1`(IN q1 int,IN q2 int,IN q3 int,IN x int,OUT okay int)
BEGIN
declare qt1 Integer;
declare qt2 Integer;
declare qt3 Integer;
select projector,marker,speaker into qt1,qt2,qt3 from logisavail;
if(q1<qt1) then
if(q2<qt2) then
if(q3<qt3) then
insert into logisreq values(x,q1,q2,q3);
set okay = 1;
end if;
end if;
else
set okay = 0;
end if;
commit;
END

#call to procedure
if request.method == "POST":
    q1=request.form["qt1"]
    q2=request.form["qt2"]
    q3=request.form["qt3"]
    sql1="call p1(%s,%s,%s,%s,@a)"%(q1,q2,q3,x)
    cursor.execute(sql1)
    sql2="select @a"
    cursor.execute(sql2)
    a=cursor.fetchall()
    if a[0][0] == 1:
        #success message
    else:
        #fail could not add message


#cursor select available room and insert new booking
CREATE DEFINER=`root`@`localhost` PROCEDURE `p2`(IN bid varchar(10),IN bookid int,IN x int, IN ename varchar(50),OUT okay int)
BEGIN
declare roomidd int;
declare stat int;
declare done INT DEFAULT FALSE;
declare cur1 cursor for select room_id,status from room where building = bid;
DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;
set okay=0;
open cur1;
read_loop: LOOP
fetch cur1 into roomidd,stat;
if stat = 0 then
insert into booking values(bookid,roomidd,x,ename);
set okay=1;
end if;
if done then
leave read_loop;
end if;
end loop;
close cur1;
commit;
END


#call to procedure
if request.method="POST":
    sql1 = "select max(booking_id)+1 from suser;"
    data1=cursor.execute(sql1)
    idd=data1[0][0]
    bid='AB2'
    sql2="call p2(%s,%s,%s,%s,@a);"%(bid,idd,x,ename)
    cursor.execute(sql2);

#trigger change status of room
Delimiter#
create or replace trigger changestatus
after update on booking
for each Row
declare
buildd varchar(10);
begin
select building into buildd from room where roomid= new.room_id;
update room set status = 1 where building= buildd and room_id= new.room_id;
end#

#trigger update available logistics table
CREATE DEFINER=`root`@`localhost` TRIGGER `logisappr_update` AFTER UPDATE ON `logisappr` FOR EACH ROW BEGIN
declare p int;
declare m int;
declare s int;
declare id int;
if(new.SC!=0 and new.CW!=0 and new.SO!=0 and new.director!=0) then 
select projector,marker,speaker into p,m,s from logisreq where sid = new.sid;
update logisavail set projector = projector - p;
update logisavail set marker = marker - m;
update logisavail set speaker = speaker - s;
end if;
END

#trigger to add tuple into bookappr when new booking is done
CREATE DEFINER=`root`@`localhost` TRIGGER `booking_approval` AFTER INSERT ON `booking` FOR EACH ROW BEGIN
insert into bookappr values(NEW.booking_id,0,0,0,0);
END

#trigger to add tuple into logisappr when new logis req is done
CREATE DEFINER=`root`@`localhost` TRIGGER `logisreq_appr` AFTER INSERT ON `logisreq` FOR EACH ROW BEGIN
declare p int;
declare s int;
declare m int;
select * from logisavail into p,m,s;
if(p>new.projector and s>new.speaker and m>new.marker) then
insert into logisappr values(new.sid,0,0,0,0);
end if;
END

#########
CREATE DEFINER=`root`@`localhost` TRIGGER `logisappr_AFTER_UPDATE` AFTER UPDATE ON `logisappr` FOR EACH ROW BEGIN
declare p1 int;
declare p2 int;
declare s1 int;
declare s2 int;
declare m1 int;
declare m2 int;
declare s int;
if(new.SC!=0 and new.CW!=0 and new.SO!=0 and new.director!=0) then 
select t.projector,t.marker,t.speaker,k.projector,k.marker,k.speaker from logisavail as t,logisreqas as k into p1,m1,s1,p2,m2,s2 where t.sid = k.sid and k.sid = new.sid;
if(s=new.sid) then
update logisavail set projector = projector - p2 where p1>p2;
update logisavail set marker = marker - m2 where m1>m2;
update logisavail set speaker = speaker - s2 where s1>s2;
end if;
end if;
END



bid='AB2'
    num = 100;
    #not inserting should check
    global ename
    #sql2="call p2(%s,%s,%s,%s,@a);"%(bid,idd,num,ename)
    #cursor.execute(sql2)
    #mydb.commit()
    return render_template('perm.html')