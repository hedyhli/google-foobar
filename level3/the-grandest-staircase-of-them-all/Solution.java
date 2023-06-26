// grandest staircase indeed... this was such an interesting puzzle!!!
// thought process: instead of going down the stairs... HOW ABOUT WE GO UP?!?!?!
// ;P
// build the stairs from bottom to top
//
// first implemented in python. after 6 iterations, it finally worked, but for larger numbers of n it took too long to evaluate (n=199 took 4 minutes)
// so then I converted it to java, and 199/200 both takes less than a minute!


class Solution {
  public static void main(String[] args) {
    System.out.println(solution(Integer.valueOf(args[0])));
  }

  public static int solution(int n) {
    int result = s(n, 1, 1, 0);
    return result;
  }

  public static int s(int n, int t, int start, int w) {
    if (start >= n || n-t <= 0 || n-t <= start) {
        return w;
    }

    w++;
    int newstart = start + 1;
    t = t + newstart;
    int w2 = s(n, t, newstart, w);
    t = t - start;
    start = start + 1;
    return s(n, t, start, w2);
  }
}
