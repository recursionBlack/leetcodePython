from myLeetcodeUtils import StockSpanner

if __name__ == "__main__":
    stockSpanner = StockSpanner()

    print(stockSpanner.next(100))  # ; // 返回1
    print(stockSpanner.next(80))   # ; // 返回1
    print(stockSpanner.next(60))   # ; // 返回1
    print(stockSpanner.next(70))   # ; // 返回2
    print(stockSpanner.next(60))   # ; // 返回1
    print(stockSpanner.next(75))   # ; // 返回4 ，因为截至今天的最后4个股价(包括今天的股价75) 都小于或等于今天的股价。
    print(stockSpanner.next(85))   # ; // 返回6