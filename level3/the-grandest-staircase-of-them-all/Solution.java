class Solution {
  public static void main(String[] args) {
    System.out.println(solution(Integer.valueOf(args[0])));
  }

  public static int solution(int n) {
    return sol(n, 1, 1, 0);
  }

  public static int sol(int n, int t, int s, int w) {
    if (s >= n || n-t <= s) {
        return w;
    }

    w = sol(n, t+s+1, s+1, w+1);
    return sol(n, t+1, s+1, w);
  }
}

// grandest staircase indeed... this was such an interesting puzzle!!!
//
// first implemented in python. after 6 iterations, it finally worked, but for larger numbers of n it took too long to evaluate (n=199 took 4 minutes)
// so then I converted it to java, and 199/200 both takes less than a minute!
