class Solution {
    public boolean isPalindrome(String s) {
        int left = 0; // index of the first char
        int right = s.length() - 1; // index of the last char


        while (left <= right) {
            boolean isFirstCharLetter = Character.isLetterOrDigit(s.charAt(left));
            boolean isSecondCharLetter = Character.isLetterOrDigit(s.charAt(right));

            if (isFirstCharLetter != true) {
                left++;
                continue;
            }
            
            if (isSecondCharLetter != true) {
                right--;
                continue;
            }

            char firstChar = Character.toLowerCase(s.charAt(left));
            char secondChar = Character.toLowerCase(s.charAt(right));
            if (firstChar != secondChar) {
                return false;
            }
            left++;
            right--;
        }

        return true;

    }
}
