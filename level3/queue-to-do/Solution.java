class Solution {
    public static int solution(int start, int length) {
        int ans = start;
        
        for (int n=1; n<=length; n++) {
            int items = -n + length + 1;
            int first = (n-1) * length + start;
            for (int x=first; x<items+first; x++) {
                ans = ans^x;
            }
        }
        
        return ans^start;
    }

    public static void main(String[] args) {
      System.out.println(Solution.solution(Integer.valueOf(args[0]), Integer.valueOf(args[1])));
    }
}
