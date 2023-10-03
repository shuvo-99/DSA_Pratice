class Solution:
    def pairWithMaxSum(self, arr, N):
        add = 0    
        for i in range(N):
            l = []
            l.append(arr[i])
            for j in range(i+1,N):
              l.append(arr[j])
              new_min1 = min(l)
              new_min1_idx = l.index(new_min1)
              l.remove(new_min1)
              new_min2 = min(l)
              l.insert(new_min1_idx,new_min1)

              new_add = new_min1 + new_min2

              if new_add > add:
                  add = new_add
        return add          

def main():

    T = 1

    while(T > 0):
        n = 5
        a = [4, 3, 1, 5, 6]
        ob=Solution()
        print(ob.pairWithMaxSum(a, n))

        T -= 1

if __name__ == "__main__":
    main()

