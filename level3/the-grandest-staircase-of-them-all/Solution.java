// grandest staircase indeed... this was such an interesting puzzle!!!
// thought process: instead of going down the stairs... HOW ABOUT WE GO UP?!?!?!
// ;P
// build the stairs from bottom to top
//
// first implemented in python. after 6 iterations, it finally worked, but for larger numbers of n it took too long to evaluate (n=199 took 4 minutes)
// so then I converted it to java, and 199/200 both takes less than a minute!


class Solution {
  public static void main(String[] args) {
    System.out.println(solution(200));
  }

  public static int solution(int n) {
    int[] result = s(n, 1, 1, 0);
    return result[0];
  }

  public static int[] s(int n, int t, int start, int w) {
    int[] ret = new int[2];
    if (start >= n || n-t <= 0 || n-t <= start) {
      t = t - start;
      ret[0] = w;
      ret[1] = start;
      return ret;
    }

    w++;
    int newstart = start + 1;
    t = t + newstart;
    int[] result = s(n, t, newstart, w);
    w = result[0];
    int oldstart = result[1];

    if (oldstart != 0) {
      t = t - start;
      start++;
      return s(n, t, start, w);
    }
    return ret;
  }
}
