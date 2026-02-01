-- Still need to take care of Wales, Northern Ireland, Scotland, and England
-- These countries should take on the values in United Kingdom

/*
Select *
From FIFA..TaxFracGDP
Where [Country Name] = 'United Kingdom'


Select * 
From FIFA..[testing out]
Where country in ('Wales', 'Northern Ireland', 'England', 'Scotland')
*/

Drop Table [UK Countries]
Go

Create Table [UK Countries]
(
    Country varchar(50)
  , Year smallint
  , TRAPGDP varchar(50)
  , TRAPGDP_invalid tinyint
)

-- 1993
Insert into [UK Countries]
Select 
    [Country] = 'Wales'
  , YEAR = 1993
  , [1993]
  , 0 
From FIFA..[TaxFracGDP] 
Where [Country Name]= 'United Kingdom'   

Insert into [UK Countries]
Select 
    [Country] = 'Northern Ireland'
  , YEAR = 1993
  , [1993]
  , 0 
From FIFA..[TaxFracGDP] 
Where [Country Name]= 'United Kingdom'   

Insert into [UK Countries]
Select 
    [Country] = 'England'
  , YEAR = 1993
  , [1993]
  , 0 
From FIFA..[TaxFracGDP] 
Where [Country Name]= 'United Kingdom'   

Insert into [UK Countries]
Select 
    [Country] = 'Scotland'
  , YEAR = 1993
  , [1993]
  , 0 
From FIFA..[TaxFracGDP] 
Where [Country Name]= 'United Kingdom'   

-- 1994
Insert into [UK Countries]
Select 
    [Country] = 'Wales'
  , YEAR = 1994
  , [1994]
  , 0 
From FIFA..[TaxFracGDP] 
Where [Country Name]= 'United Kingdom'   

Insert into [UK Countries]
Select 
    [Country] = 'Northern Ireland'
  , YEAR = 1994
  , [1994]
  , 0 
From FIFA..[TaxFracGDP] 
Where [Country Name]= 'United Kingdom'   

Insert into [UK Countries]
Select 
    [Country] = 'England'
  , YEAR = 1994
  , [1994]
  , 0 
From FIFA..[TaxFracGDP] 
Where [Country Name]= 'United Kingdom'   

Insert into [UK Countries]
Select 
    [Country] = 'Scotland'
  , YEAR = 1994
  , [1994]
  , 0 
From FIFA..[TaxFracGDP] 
Where [Country Name]= 'United Kingdom'   

-- 1995
Insert into [UK Countries]
Select 
    [Country] = 'Wales'
  , YEAR = 1995
  , [1995]
  , 0 
From FIFA..[TaxFracGDP] 
Where [Country Name]= 'United Kingdom'   

Insert into [UK Countries]
Select 
    [Country] = 'Northern Ireland'
  , YEAR = 1995
  , [1995]
  , 0 
From FIFA..[TaxFracGDP] 
Where [Country Name]= 'United Kingdom'   

Insert into [UK Countries]
Select 
    [Country] = 'England'
  , YEAR = 1995
  , [1995]
  , 0 
From FIFA..[TaxFracGDP] 
Where [Country Name]= 'United Kingdom'   

Insert into [UK Countries]
Select 
    [Country] = 'Scotland'
  , YEAR = 1995
  , [1995]
  , 0 
From FIFA..[TaxFracGDP] 
Where [Country Name]= 'United Kingdom'   

-- 1996
Insert into [UK Countries]
Select 
    [Country] = 'Wales'
  , YEAR = 1996
  , [1996]
  , 0 
From FIFA..[TaxFracGDP] 
Where [Country Name]= 'United Kingdom'   

Insert into [UK Countries]
Select 
    [Country] = 'Northern Ireland'
  , YEAR = 1996
  , [1996]
  , 0 
From FIFA..[TaxFracGDP] 
Where [Country Name]= 'United Kingdom'   

Insert into [UK Countries]
Select 
    [Country] = 'England'
  , YEAR = 1996
  , [1996]
  , 0 
From FIFA..[TaxFracGDP] 
Where [Country Name]= 'United Kingdom'   

Insert into [UK Countries]
Select 
    [Country] = 'Scotland'
  , YEAR = 1996
  , [1996]
  , 0 
From FIFA..[TaxFracGDP] 
Where [Country Name]= 'United Kingdom'   

-- 1997
Insert into [UK Countries]
Select 
    [Country] = 'Wales'
  , YEAR = 1997
  , [1997]
  , 0 
From FIFA..[TaxFracGDP] 
Where [Country Name]= 'United Kingdom'   

Insert into [UK Countries]
Select 
    [Country] = 'Northern Ireland'
  , YEAR = 1997
  , [1997]
  , 0 
From FIFA..[TaxFracGDP] 
Where [Country Name]= 'United Kingdom'   

Insert into [UK Countries]
Select 
    [Country] = 'England'
  , YEAR = 1997
  , [1997]
  , 0 
From FIFA..[TaxFracGDP] 
Where [Country Name]= 'United Kingdom'   

Insert into [UK Countries]
Select 
    [Country] = 'Scotland'
  , YEAR = 1997
  , [1997]
  , 0 
From FIFA..[TaxFracGDP] 
Where [Country Name]= 'United Kingdom'   

-- 1998
Insert into [UK Countries]
Select 
    [Country] = 'Wales'
  , YEAR = 1998
  , [1998]
  , 0 
From FIFA..[TaxFracGDP] 
Where [Country Name]= 'United Kingdom'   

Insert into [UK Countries]
Select 
    [Country] = 'Northern Ireland'
  , YEAR = 1998
  , [1998]
  , 0 
From FIFA..[TaxFracGDP] 
Where [Country Name]= 'United Kingdom'   

Insert into [UK Countries]
Select 
    [Country] = 'England'
  , YEAR = 1998
  , [1998]
  , 0 
From FIFA..[TaxFracGDP] 
Where [Country Name]= 'United Kingdom'   

Insert into [UK Countries]
Select 
    [Country] = 'Scotland'
  , YEAR = 1998
  , [1998]
  , 0 
From FIFA..[TaxFracGDP] 
Where [Country Name]= 'United Kingdom'   

-- 1999
Insert into [UK Countries]
Select 
    [Country] = 'Wales'
  , YEAR = 1999
  , [1999]
  , 0 
From FIFA..[TaxFracGDP] 
Where [Country Name]= 'United Kingdom'   

Insert into [UK Countries]
Select 
    [Country] = 'Northern Ireland'
  , YEAR = 1999
  , [1999]
  , 0 
From FIFA..[TaxFracGDP] 
Where [Country Name]= 'United Kingdom'   

Insert into [UK Countries]
Select 
    [Country] = 'England'
  , YEAR = 1999
  , [1999]
  , 0 
From FIFA..[TaxFracGDP] 
Where [Country Name]= 'United Kingdom'   

Insert into [UK Countries]
Select 
    [Country] = 'Scotland'
  , YEAR = 1999
  , [1999]
  , 0 
From FIFA..[TaxFracGDP] 
Where [Country Name]= 'United Kingdom'   

-- 2000
Insert into [UK Countries]
Select 
    [Country] = 'Wales'
  , YEAR = 2000
  , [2000]
  , 0 
From FIFA..[TaxFracGDP] 
Where [Country Name]= 'United Kingdom'   

Insert into [UK Countries]
Select 
    [Country] = 'Northern Ireland'
  , YEAR = 2000
  , [2000]
  , 0 
From FIFA..[TaxFracGDP] 
Where [Country Name]= 'United Kingdom'   

Insert into [UK Countries]
Select 
    [Country] = 'England'
  , YEAR = 2000
  , [2000]
  , 0 
From FIFA..[TaxFracGDP] 
Where [Country Name]= 'United Kingdom'   

Insert into [UK Countries]
Select 
    [Country] = 'Scotland'
  , YEAR = 2000
  , [2000]
  , 0 
From FIFA..[TaxFracGDP] 
Where [Country Name]= 'United Kingdom'   

-- 2001
Insert into [UK Countries]
Select 
    [Country] = 'Wales'
  , YEAR = 2001
  , [2001]
  , 0 
From FIFA..[TaxFracGDP] 
Where [Country Name]= 'United Kingdom'   

Insert into [UK Countries]
Select 
    [Country] = 'Northern Ireland'
  , YEAR = 2001
  , [2001]
  , 0 
From FIFA..[TaxFracGDP] 
Where [Country Name]= 'United Kingdom'   

Insert into [UK Countries]
Select 
    [Country] = 'England'
  , YEAR = 2001
  , [2001]
  , 0 
From FIFA..[TaxFracGDP] 
Where [Country Name]= 'United Kingdom'   

Insert into [UK Countries]
Select 
    [Country] = 'Scotland'
  , YEAR = 2001
  , [2001]
  , 0 
From FIFA..[TaxFracGDP] 
Where [Country Name]= 'United Kingdom'   

-- 2002
Insert into [UK Countries]
Select 
    [Country] = 'Wales'
  , YEAR = 2002
  , [2002]
  , 0 
From FIFA..[TaxFracGDP] 
Where [Country Name]= 'United Kingdom'   

Insert into [UK Countries]
Select 
    [Country] = 'Northern Ireland'
  , YEAR = 2002
  , [2002]
  , 0 
From FIFA..[TaxFracGDP] 
Where [Country Name]= 'United Kingdom'   

Insert into [UK Countries]
Select 
    [Country] = 'England'
  , YEAR = 2002
  , [2002]
  , 0 
From FIFA..[TaxFracGDP] 
Where [Country Name]= 'United Kingdom'   

Insert into [UK Countries]
Select 
    [Country] = 'Scotland'
  , YEAR = 2002
  , [2002]
  , 0 
From FIFA..[TaxFracGDP] 
Where [Country Name]= 'United Kingdom'   

-- 2003
Insert into [UK Countries]
Select 
    [Country] = 'Wales'
  , YEAR = 2003
  , [2003]
  , 0 
From FIFA..[TaxFracGDP] 
Where [Country Name]= 'United Kingdom'   

Insert into [UK Countries]
Select 
    [Country] = 'Northern Ireland'
  , YEAR = 2003
  , [2003]
  , 0 
From FIFA..[TaxFracGDP] 
Where [Country Name]= 'United Kingdom'   

Insert into [UK Countries]
Select 
    [Country] = 'England'
  , YEAR = 2003
  , [2003]
  , 0 
From FIFA..[TaxFracGDP] 
Where [Country Name]= 'United Kingdom'   

Insert into [UK Countries]
Select 
    [Country] = 'Scotland'
  , YEAR = 2003
  , [2003]
  , 0 
From FIFA..[TaxFracGDP] 
Where [Country Name]= 'United Kingdom'   

-- 2004
Insert into [UK Countries]
Select 
    [Country] = 'Wales'
  , YEAR = 2004
  , [2004]
  , 0 
From FIFA..[TaxFracGDP] 
Where [Country Name]= 'United Kingdom'   

Insert into [UK Countries]
Select 
    [Country] = 'Northern Ireland'
  , YEAR = 2004
  , [2004]
  , 0 
From FIFA..[TaxFracGDP] 
Where [Country Name]= 'United Kingdom'   

Insert into [UK Countries]
Select 
    [Country] = 'England'
  , YEAR = 2004
  , [2004]
  , 0 
From FIFA..[TaxFracGDP] 
Where [Country Name]= 'United Kingdom'   

Insert into [UK Countries]
Select 
    [Country] = 'Scotland'
  , YEAR = 2004
  , [2004]
  , 0 
From FIFA..[TaxFracGDP] 
Where [Country Name]= 'United Kingdom'   

-- 2005
Insert into [UK Countries]
Select 
    [Country] = 'Wales'
  , YEAR = 2005
  , [2005]
  , 0 
From FIFA..[TaxFracGDP] 
Where [Country Name]= 'United Kingdom'   

Insert into [UK Countries]
Select 
    [Country] = 'Northern Ireland'
  , YEAR = 2005
  , [2005]
  , 0 
From FIFA..[TaxFracGDP] 
Where [Country Name]= 'United Kingdom'   

Insert into [UK Countries]
Select 
    [Country] = 'England'
  , YEAR = 2005
  , [2005]
  , 0 
From FIFA..[TaxFracGDP] 
Where [Country Name]= 'United Kingdom'   

Insert into [UK Countries]
Select 
    [Country] = 'Scotland'
  , YEAR = 2005
  , [2005]
  , 0 
From FIFA..[TaxFracGDP] 
Where [Country Name]= 'United Kingdom'   

-- 2006
Insert into [UK Countries]
Select 
    [Country] = 'Wales'
  , YEAR = 2006
  , [2006]
  , 0 
From FIFA..[TaxFracGDP] 
Where [Country Name]= 'United Kingdom'   

Insert into [UK Countries]
Select 
    [Country] = 'Northern Ireland'
  , YEAR = 2006
  , [2006]
  , 0 
From FIFA..[TaxFracGDP] 
Where [Country Name]= 'United Kingdom'   

Insert into [UK Countries]
Select 
    [Country] = 'England'
  , YEAR = 2006
  , [2006]
  , 0 
From FIFA..[TaxFracGDP] 
Where [Country Name]= 'United Kingdom'   

Insert into [UK Countries]
Select 
    [Country] = 'Scotland'
  , YEAR = 2006
  , [2006]
  , 0 
From FIFA..[TaxFracGDP] 
Where [Country Name]= 'United Kingdom'   

-- 2007
Insert into [UK Countries]
Select 
    [Country] = 'Wales'
  , YEAR = 2007
  , [2007]
  , 0 
From FIFA..[TaxFracGDP] 
Where [Country Name]= 'United Kingdom'   

Insert into [UK Countries]
Select 
    [Country] = 'Northern Ireland'
  , YEAR = 2007
  , [2007]
  , 0 
From FIFA..[TaxFracGDP] 
Where [Country Name]= 'United Kingdom'   

Insert into [UK Countries]
Select 
    [Country] = 'England'
  , YEAR = 2007
  , [2007]
  , 0 
From FIFA..[TaxFracGDP] 
Where [Country Name]= 'United Kingdom'   

Insert into [UK Countries]
Select 
    [Country] = 'Scotland'
  , YEAR = 2007
  , [2007]
  , 0 
From FIFA..[TaxFracGDP] 
Where [Country Name]= 'United Kingdom'   

-- 2008
Insert into [UK Countries]
Select 
    [Country] = 'Wales'
  , YEAR = 2008
  , [2008]
  , 0 
From FIFA..[TaxFracGDP] 
Where [Country Name]= 'United Kingdom'   

Insert into [UK Countries]
Select 
    [Country] = 'Northern Ireland'
  , YEAR = 2008
  , [2008]
  , 0 
From FIFA..[TaxFracGDP] 
Where [Country Name]= 'United Kingdom'   

Insert into [UK Countries]
Select 
    [Country] = 'England'
  , YEAR = 2008
  , [2008]
  , 0 
From FIFA..[TaxFracGDP] 
Where [Country Name]= 'United Kingdom'   

Insert into [UK Countries]
Select 
    [Country] = 'Scotland'
  , YEAR = 2008
  , [2008]
  , 0 
From FIFA..[TaxFracGDP] 
Where [Country Name]= 'United Kingdom'   

-- 2009
Insert into [UK Countries]
Select 
    [Country] = 'Wales'
  , YEAR = 2009
  , [2009]
  , 0 
From FIFA..[TaxFracGDP] 
Where [Country Name]= 'United Kingdom'   

Insert into [UK Countries]
Select 
    [Country] = 'Northern Ireland'
  , YEAR = 2009
  , [2009]
  , 0 
From FIFA..[TaxFracGDP] 
Where [Country Name]= 'United Kingdom'   

Insert into [UK Countries]
Select 
    [Country] = 'England'
  , YEAR = 2009
  , [2009]
  , 0 
From FIFA..[TaxFracGDP] 
Where [Country Name]= 'United Kingdom'   

Insert into [UK Countries]
Select 
    [Country] = 'Scotland'
  , YEAR = 2009
  , [2009]
  , 0 
From FIFA..[TaxFracGDP] 
Where [Country Name]= 'United Kingdom'   

-- 2010
Insert into [UK Countries]
Select 
    [Country] = 'Wales'
  , YEAR = 2010
  , [2010]
  , 0 
From FIFA..[TaxFracGDP] 
Where [Country Name]= 'United Kingdom'   

Insert into [UK Countries]
Select 
    [Country] = 'Northern Ireland'
  , YEAR = 2010
  , [2010]
  , 0 
From FIFA..[TaxFracGDP] 
Where [Country Name]= 'United Kingdom'   

Insert into [UK Countries]
Select 
    [Country] = 'England'
  , YEAR = 2010
  , [2010]
  , 0 
From FIFA..[TaxFracGDP] 
Where [Country Name]= 'United Kingdom'   

Insert into [UK Countries]
Select 
    [Country] = 'Scotland'
  , YEAR = 2010
  , [2010]
  , 0 
From FIFA..[TaxFracGDP] 
Where [Country Name]= 'United Kingdom'   

-- 2011
Insert into [UK Countries]
Select 
    [Country] = 'Wales'
  , YEAR = 2011
  , [2011]
  , 0 
From FIFA..[TaxFracGDP] 
Where [Country Name]= 'United Kingdom'   

Insert into [UK Countries]
Select 
    [Country] = 'Northern Ireland'
  , YEAR = 2011
  , [2011]
  , 0 
From FIFA..[TaxFracGDP] 
Where [Country Name]= 'United Kingdom'   

Insert into [UK Countries]
Select 
    [Country] = 'England'
  , YEAR = 2011
  , [2011]
  , 0 
From FIFA..[TaxFracGDP] 
Where [Country Name]= 'United Kingdom'   

Insert into [UK Countries]
Select 
    [Country] = 'Scotland'
  , YEAR = 2011
  , [2011]
  , 0 
From FIFA..[TaxFracGDP] 
Where [Country Name]= 'United Kingdom'   

Select * From [UK Countries]
Order by Country