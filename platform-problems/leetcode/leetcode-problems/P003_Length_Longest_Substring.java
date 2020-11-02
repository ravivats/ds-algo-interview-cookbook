import java.util.Arrays;

class P003_Length_Longest_Substring {
    static final int TOTAL_CHAR = 256;

    public int lengthOfLongestSubstring(String s) {
        if (s == null || s.length() == 0) {
            return 0;
        }
        int max = 0, startWindow = 0;
        int[] lastIndex = new int[TOTAL_CHAR];
        Arrays.fill(lastIndex, -1);

        for (int j = 0; j < s.length(); j++) {
            startWindow = Math.max(startWindow, lastIndex[s.charAt(j)] + 1);
            max = Math.max(max, j + 1 - startWindow);
            lastIndex[s.charAt(j)] = j;
        }
        return max;
    }
}