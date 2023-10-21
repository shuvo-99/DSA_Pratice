class Solution:
    def generate(self, numRows):
        matrix = []
        for  i in range(1,numRows+1):
            elem = []
            if i == 1:                                       # for 1st row default set value [1]
                elem.append(1)
                matrix.append(elem)                          # Add the row in the matrix
            
            elif i == 2:                                     # for 2nd row, default set value [1,1]
                elem.append(1)
                elem.append(1)
                matrix.append(elem)                          # Add the row in the matrix
            
            else:
              for j in range(len(matrix[i-2])):              # for rest of the row, iterate loop equal to length of its previous row
                if j == 0:                                   # for 1st col, default set value 1
                  elem.append(1)  
                else:
                  val = matrix[i-2][j-1] + matrix[i-2][j]    # for rest col, add current col (j) value with its prev col (j-1) value of the previous row
                  elem.append(val)                           # then store the value in the current col value of current row (elem)
                  
              elem.append(1)                                 # for last col, default set value 1
              matrix.append(elem)                            # Add the row in the matrix
                    
                
        print(matrix)    
                            
    
obj = Solution()
obj.generate(5)