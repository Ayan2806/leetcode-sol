class Solution {
    public int reverse(int x) {
        int rev = 0;

        while (x != 0) {
            int digit = x % 10;
            int temp = rev * 10 + digit;

            // Check for overflow
            if ((temp - digit) / 10 != rev)
                return 0;

            rev = temp;
            x /= 10;
        }

        return rev;
    }
}
