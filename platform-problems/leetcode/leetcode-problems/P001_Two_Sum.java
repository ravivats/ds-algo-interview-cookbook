import java.util.Arrays;

/**
 * Given an array of integers nums and an integer target, return indices of the
 * two numbers such that they add up to target.
 * 
 * You may assume that each input would have exactly one solution, and you may
 * not use the same element twice.
 * 
 * You can return the answer in any order.
 * 
 * Input: nums = [2,7,11,15], target = 9
 * 
 * Output: [0,1]
 * 
 * Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
 */

public class P001_Two_Sum {
    public static int[] twoSum(int[] nums, int target) {
        Arrays.sort(nums);
        int low = 0, high = nums.length - 1;
        while (low < high) {
            if (nums[low] + nums[high] == target)
                return new int[] { low, high };
            else if (nums[low] + nums[high] > target)
                high--;
            else
                low++;
        }
        return new int[] { 0, 0 };
    }

    public static void main(String[] args) {
        int[] result = twoSum(new int[] { 2, 11, 7, 15 }, 9);
        for (int i : result) {
            System.out.println(i);
        }
    }
}
