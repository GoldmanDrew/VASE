create table if not exists companies(
Ticker varchar(5), 
ClassName varchar(100), 
Department varchar(100), 
Shares int, 
ShortFee decimal(2,2) default 0, 
primary key (Ticker)
);

create table if not exists agents(
ID int AUTO_INCREMENT, 
Agent varchar(20) NOT NULL, 
Cash int default 0, 
Wealth int default 0, 
Email varchar(70),
primary key (ID), 
unique key (Agent)
);

create table if not exists agentshares(
ID int AUTO_INCREMENT , 
Agent_id varchar(20), 
Company_id varchar(20), 
Shares int default 0, 
Borrowed int default 0, 
Collateral int default 0, 
PRIMARY KEY (ID), 
FOREIGN KEY (Agent_id) REFERENCES agents(Agent) ON UPDATE CASCADE ON DELETE CASCADE, 
FOREIGN KEY (Company_id) REFERENCES companies(Ticker) ON UPDATE CASCADE ON DELETE CASCADE, 
UNIQUE KEY (Agent_id,Company_id) 
);

create table if not exists orders(
OrderBookName_id varchar(20) NOT NULL, 
Agent_id varchar(20) NOT NULL, 
OrderID int NOT NULL AUTO_INCREMENT, 
Type varchar(1), 
Direction varchar(20), 
Price int, 
Quantity int, 
QuantityToFill int, 
Filled varchar(1) DEFAULT 'N', 
IDtoCancel int, 
Time timestamp DEFAULT current_timestamp, 
PRIMARY KEY (OrderID), 
FOREIGN KEY (Agent_id) REFERENCES agents(Agent) ON UPDATE CASCADE ON DELETE CASCADE, 
FOREIGN KEY (OrderBookName_id) REFERENCES companies(Ticker) ON UPDATE CASCADE ON DELETE CASCADE 
 );

create table if not exists prices(
 OrderBookName varchar(20) NOT NULL, 
Price int(20), 
Quantity int(20), 
DirectionTrigger varchar(1), 
Asker varchar(20), 
Asker_OrderID_id int(20), 
Bidder varchar(20), 
Bidder_OrderID_id int(20), 
BestAsk int(20), 
BestBid int(20), 
Time timestamp DEFAULT current_timestamp, 
FillID int NOT NULL AUTO_INCREMENT, 
PRIMARY KEY (FillID), 
FOREIGN KEY (Asker_OrderID_id) REFERENCES orders(OrderID) ON UPDATE CASCADE ON DELETE CASCADE, 
FOREIGN KEY (Bidder_OrderID_id) REFERENCES orders(OrderID) ON UPDATE CASCADE ON DELETE CASCADE 
);
