import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

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
    public static int[] twoSumReturnNumbers(int[] nums, int target) {
        Arrays.sort(nums);
        int low = 0, high = nums.length - 1;
        while (low < high) {
            if (nums[low] + nums[high] == target)
                return new int[] { nums[low], nums[high] };
            else if (nums[low] + nums[high] > target)
                high--;
            else
                low++;
        }
        return new int[] { 0, 0 };
    }

    public static int[] twoSumReturnIndices(int[] nums, int target) {
        Map<Integer, Integer> map = new HashMap<Integer, Integer>();
        for (int i = 0; i < nums.length; i++) {
            int diff = target - nums[i];
            Integer index = map.get(diff);
            if (index != null)
                return new int[] { i, index };
            map.put(nums[i], i);
        }
        return new int[] { 0, 0 };
    }

    public static void main(String[] args) {
        int[] numbers = twoSumReturnNumbers(new int[] { 2, 11, 7, 15 }, 9);
        int[] indices = twoSumReturnIndices(new int[] { 2, 11, 7, 15 }, 9);
        for (int i =0 ; i<2; i++){
            System.out.printf("Num: %d, Index: %d\n", numbers[i], indices[i]);
        }
    }
}
