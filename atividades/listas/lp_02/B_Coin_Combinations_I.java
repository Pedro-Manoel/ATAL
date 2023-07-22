import java.io.DataInputStream;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.Arrays;

public class CoinCombinations {

  static class Reader {

    private final int BUFFER_SIZE = 1 << 16;
    private DataInputStream din;
    private byte[] buffer;
    private int bufferPointer, bytesRead;

    public Reader() {
      din = new DataInputStream(System.in);
      buffer = new byte[BUFFER_SIZE];
      bufferPointer = bytesRead = 0;
    }

    public int nextInt() throws IOException {
      int ret = 0;
      byte c = read();
      while (c <= ' ') {
        c = read();
      }
      boolean neg = (c == '-');
      if (neg) c = read();
      do {
        ret = ret * 10 + c - '0';
      } while ((c = read()) >= '0' && c <= '9');

      if (neg) return -ret;
      return ret;
    }

    private void fillBuffer() throws IOException {
      bytesRead = din.read(buffer, bufferPointer = 0, BUFFER_SIZE);
      if (bytesRead == -1) buffer[0] = -1;
    }

    private byte read() throws IOException {
      if (bufferPointer == bytesRead) fillBuffer();
      return buffer[bufferPointer++];
    }
  }

  public static void main(String[] args) throws IOException {
    Reader in = new Reader();
    PrintWriter out = new PrintWriter(System.out);

    int n = in.nextInt();
    int value = in.nextInt();

    int[] memo = new int[value + 1];
    int[] coins = new int[n];

    for (int i = 0; i < n; i++) {
      coins[i] = in.nextInt();
    }

    Arrays.sort(coins);

    memo[0] = 1;
    for (int i = 1; i <= value; i++) {
      for (int j = 0; j < n; j++) {
        if (i - coins[j] >= 0) {
          memo[i] = (memo[i] + memo[i - coins[j]]);
          if (memo[i] > (int) 1e9 + 7) {
            memo[i] -= (int) 1e9 + 7;
          }
        } else {
          break;
        }
      }
    }

    out.println(memo[value]);
    out.close();
  }
}
