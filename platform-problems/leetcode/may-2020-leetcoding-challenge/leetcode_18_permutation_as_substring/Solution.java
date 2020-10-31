package leetcode_18_permutation_as_substring;

import java.util.HashMap;

public class Solution {

    public boolean checkAllValues(HashMap<Character, Integer> map, char[] arr, int index) {
        while(index < arr.length) {
            if (map.containsKey(arr[index])) {
                Integer value = map.get(arr[index]); 
                if (value <= 1) {
                    map.remove(arr[index]);    
                } else {
                    map.put(arr[index], value-1);
                }
                index += 1;
            } else {
                break;
            }
        }
        return map.isEmpty();
    }

    public boolean checkInclusion(String s1, String s2) {
        HashMap<Character,Integer> charMap = new HashMap<>();
        for (char c : s1.toCharArray()) {
            if (charMap.containsKey(c)) {
                int value = charMap.get(c);
                charMap.put(c, value + 1);
            } else {
                charMap.put(c, 1);
            }
        }

        char[] arr = s2.toCharArray();
        for (int i = 0; i < arr.length; i++) {
            if (charMap.containsKey(arr[i])) {
                HashMap<Character, Integer> cloneCharMap = (HashMap<Character,Integer>)charMap.clone();
                if (checkAllValues(cloneCharMap, arr, i)) {
                    return true;
                };
            }
        }
        return false;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.checkInclusion("ab", "eidbaooo")); // should be true
        System.out.println(sol.checkInclusion("ab", "eidboaoo")); // should be false
        System.out.println(sol.checkInclusion("adc", "dcda")); // should be true
        System.out.println(sol.checkInclusion("hello", "ooolleoooleh")); // should be false
    }
}
