-- 1.	Stores Countries' Statistics (Population and Reputation):
drop table [dbo].[countries]
CREATE TABLE [dbo].[countries] (
    CountryName varchar(255) NOT NULL,
    Population numeric NULL,
    UserCount numeric NULL,
    UserReputation numeric NULL
);

-- 2.	Stores Countries' top users:
drop table [dbo].[countries_top_users]
CREATE TABLE [dbo].[countries_top_users] (
    CountryName varchar(255) NOT NULL,
    UserId numeric NOT NULL,
    UserDisplayName varchar(255) NOT NULL,
    UserReputation numeric NULL,
    UserViews numeric NULL,
    UserUpvotes numeric NULL,
    UserDownvotes numeric NULL,
    UserRank numeric NOT NULL
);

-- 3.	Stores Topics every day:
drop table [dbo].[topics]
CREATE TABLE [dbo].[topics] (
    topic varchar(255) NULL,
    quantity numeric NULL,
    trainingDate date NULL
);
