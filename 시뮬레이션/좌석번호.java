import java.util.Arrays;

class 좌석번호 {
    public int[] solution(int c, int r, int k) {
        if (k > c * r) return new int[]{0, 0}; // 좌석 초과 시 즉시 반환

        int[][] arr = new int[c][r];
        int[] dx = {0, 1, 0, -1}; // 우, 하, 좌, 상 순서
        int[] dy = {1, 0, -1, 0};
        int dir = 0;
        int xx = 0, yy = 0;

        for (int i = 0; i < k - 1; i++) {
            arr[xx][yy] = 1;
            int nx = xx + dx[dir];
            int ny = yy + dy[dir];

            if (nx < 0 || ny < 0 || nx >= c || ny >= r || arr[nx][ny] == 1) {
                dir = (dir + 1) % 4;
                nx = xx + dx[dir];
                ny = yy + dy[dir]; // 한 번 더 이동 좌표 설정
            }

            xx = nx;
            yy = ny;
        }

        return new int[]{xx + 1, yy + 1}; // 1-based 좌표 반환
    }

    public static void main(String[] args) {
        좌석번호 T = new 좌석번호();
        System.out.println(Arrays.toString(T.solution(6, 5, 12))); // [6, 3]
        System.out.println(Arrays.toString(T.solution(6, 5, 20))); // [2, 3]
        System.out.println(Arrays.toString(T.solution(6, 5, 30))); // [0, 0]
        System.out.println(Arrays.toString(T.solution(6, 5, 31))); // [0, 0]
    }
}
