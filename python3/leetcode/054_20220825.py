class Solution:
    def spiralOrder(self, matrix):
        left, right = 0, len(matrix) - 1
        list = []
        while left <= right:

            # 1: right
            if matrix[left]:
                list += matrix[left]
                matrix[left] = []
                left += 1
            else:
                break

            # 2: down
            if left > right:
                break
            index = left
            while index < right and matrix[index]:
                list += [matrix[index][-1]]
                matrix[index].pop()
                index += 1
            if index == right and matrix[index]:
                list += [matrix[index][-1]]
                matrix[index].pop()
            if not matrix[index]:
                right -= 1
            
            # 3: left
            if matrix[right]:
                list += matrix[right][::-1]
                matrix[right] = []
                right -= 1
            else:
                break

            # 4: up
            if left > right:
                break
            index = right
            while index > left and matrix[index]:
                list += [matrix[index][0]]
                matrix[index] = matrix[index][1:]
                index -= 1
            if index == left and matrix[index]:
                list += [matrix[index][0]]
                matrix[index] = matrix[index][1:]
            if not matrix[index]:
                left += 1
        
        return list

if __name__ == "__main__":
    Test = Solution()
    print(Test.spiralOrder([[1]]))