Attribute VB_Name = "Module1"
Sub Stock()
    Dim TotalVolume As Double
    Dim i, j As Integer
    
    Cells(1, 9).Value = "Ticker"
    Cells(1, 10).Value = "Total Stock Volume"
    
    i = 2
    j = 2
    TotalVolume = Cells(2, 7).Value
    
    Do While Cells(i, 1).Value <> ""
        If Cells(i, 1).Value = Cells(i + 1, 1).Value Then
                TotalVolume = TotalVolume + Cells(i + 1, 7).Value
        Else
            Cells(j, 9).Value = Cells(i, 1).Value
            Cells(j, 10).Value = TotalVolume
            j = j + 1
            TotalVolume = Cells(i + 1, 7).Value
        End If
        
        i = i + 1
    Loop
    
End Sub
