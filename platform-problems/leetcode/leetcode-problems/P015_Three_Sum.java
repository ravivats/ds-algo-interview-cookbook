import java.util.Arrays;
import java.util.LinkedList;
import java.util.List;

/**
 * Given an array nums of n integers, are there elements a, b, c in nums 
 * such that a + b + c = 0? Find all unique triplets in the array 
 * which gives the sum of zero.
 * 
 * Notice that the solution set must not contain duplicate triplets.
 * 
 * Example 1:
 * Input: nums = [-1,0,1,2,-1,-4]
 * Output: [[-1,-1,2],[-1,0,1]]
 */

public class P015_Three_Sum {
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> resultList = new LinkedList<>();

        for (int i = 0; i < nums.length - 2; i++) {
            if (i == 0 || (i > 0 && nums[i] != nums[i - 1])) {
                int low = i + 1;
                int high = nums.length - 1;
                int sum = 0 - nums[i];
                while (low < high) {
                    if (nums[low] + nums[high] == sum) {
                        resultList.add(Arrays.asList(nums[i], nums[low], nums[high]));
                        while (low < high && nums[low] == nums[low + 1])
                            low++;
                        while (low < high && nums[high] == nums[high - 1])
                            high--;
                        low++;
                        high--;
                    } else if (nums[low] + nums[high] > sum) {
                        high--;
                    } else {
                        low++;
                    }
                }
            }
        }
        return resultList;
    }
}
