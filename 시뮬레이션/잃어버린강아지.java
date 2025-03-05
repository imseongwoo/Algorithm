import java.util.*;

class 잃어버린강아지 {
    public int solution(int[][] board) {
        int[] dx = {-1, 0, 1, 0}; // 북, 동, 남, 서
        int[] dy = {0, 1, 0, -1};
        int length = board.length;
        int hx = 0, hy = 0, hd = 0; // 현수 위치 및 방향
        int px = 0, py = 0, pd = 0; // 강아지 위치 및 방향

        // 현수와 강아지 위치 찾기
        for (int x = 0; x < length; x++) {
            for (int y = 0; y < length; y++) {
                if (board[x][y] == 2) {
                    hx = x;
                    hy = y;
                } else if (board[x][y] == 3) {
                    px = x;
                    py = y;
                }
            }
        }

        for (int time = 0; time <= 10000; time++) {
            if (hx == px && hy == py) return time; // 만남 체크

            // 현수 이동
            int nhx = hx + dx[hd];
            int nhy = hy + dy[hd];
            if (nhx < 0 || nhy < 0 || nhx >= length || nhy >= length || board[nhx][nhy] == 1) {
                hd = (hd + 1) % 4; // 시계 방향 회전
            } else {
                hx = nhx;
                hy = nhy;
            }

            // 강아지 이동
            int npx = px + dx[pd];
            int npy = py + dy[pd];
            if (npx < 0 || npy < 0 || npx >= length || npy >= length || board[npx][npy] == 1) {
                pd = (pd + 1) % 4; // 시계 방향 회전
            } else {
                px = npx;
                py = npy;
            }
        }

        return 0; // 10000번 반복 후에도 못 만나면 0 반환
    }

    public static void main(String[] args) {
        잃어버린강아지 T = new 잃어버린강아지();
        int[][] arr1 = {
                {0, 0, 0, 0, 0, 0, 1, 0, 0, 0},
                {0, 0, 0, 0, 1, 0, 0, 0, 0, 0},
                {0, 0, 0, 1, 0, 0, 0, 1, 0, 0},
                {0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
                {0, 0, 0, 1, 0, 0, 0, 2, 0, 0},
                {1, 0, 0, 0, 0, 0, 1, 0, 0, 0},
                {0, 0, 0, 1, 0, 0, 0, 0, 0, 0},
                {0, 0, 0, 0, 0, 3, 0, 0, 0, 1},
                {0, 0, 0, 1, 0, 1, 0, 0, 0, 0},
                {0, 1, 0, 1, 0, 0, 0, 0, 0, 0}};
        System.out.println(T.solution(arr1)); // 51

        int[][] arr2 = {
                {1, 0, 0, 0, 1, 0, 0, 0, 0, 0},
                {0, 0, 0, 0, 0, 0, 1, 0, 0, 0},
                {0, 0, 1, 1, 0, 0, 0, 1, 0, 0},
                {0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
                {0, 0, 0, 1, 0, 1, 0, 0, 0, 0},
                {1, 0, 0, 0, 0, 0, 1, 0, 1, 0},
                {0, 0, 0, 1, 0, 0, 0, 0, 0, 0},
                {0, 0, 1, 0, 0, 0, 0, 0, 2, 1},
                {0, 0, 0, 1, 0, 1, 0, 0, 0, 1},
                {0, 1, 0, 1, 0, 0, 0, 0, 0, 3}};
        System.out.println(T.solution(arr2)); // 17
    }
}
