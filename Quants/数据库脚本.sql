--With tmp1 as
--(
--SELECT
--[Code]
--,CONVERT(varchar(100),Cast([date] as datetime),111) as [Trade_Date]
--,[Open]
--,[High]
--,[Close]
--,[Low]
--,Round([Volume]/100,0) as Volume
--,Round([Volume]*100/([Turnover]*1000000),1) AS  Circulation_Volume
--,Round([Volume]*[Close]*100/([Turnover]*1000000),1) as Circulation_Value
--,[price_change] as [Price_Change]
--,[p_change] as [P_Change]
--,[MA5]
--,[MA10]
--,[MA20]
--,Round([V_MA5]/100,0) as [V_MA5]
--,Round([V_MA10]/100,0) as [V_MA10]
--,Round([V_MA20]/100,0) as [V_MA20]
--,[Turnover] as [Turnover] 
--FROM HistData 
--WHERE cast(DATE AS DATETIME)='2017-2-15' and [Turnover]<>0
--)

Select * From V_HistData
Where [Close]<=10 and [Circulation_Value]<=100 and [Circulation_Volume]<=10
and [MA5]>[MA10] and [MA10]>[MA20]
and Type in ('创业板','沪市A股','深市A股','中小板')
Order by [Close] asc

--Select Type,Count(*) from V_HistData
----Where [Close]<=20 and [Circulation_Value]<=100 and [Circulation_Volume]<=10 and [MA5]>[MA10] and [MA10]>[MA20]
--Group by Type