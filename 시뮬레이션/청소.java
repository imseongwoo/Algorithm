import java.util.*;

class Solution2 {
    public int[] solution(int[][] board, int k) {
        int[] answer = new int[2];

        // 이동 방향 (우, 하, 좌, 상)
        int[] dx = {0, 1, 0, -1};
        int[] dy = {1, 0, -1, 0};

        int x = 0, y = 0;  // 로봇 시작 위치
        int dir = 0;  // 초기 방향: 오른쪽(동쪽)

        int length = board.length;

        while (k > 0) {
            int nx = x + dx[dir];
            int ny = y + dy[dir];

            // 이동 가능 여부 확인
            if (nx < 0 || ny < 0 || nx >= length || ny >= length || board[nx][ny] == 1) {
                // 이동 불가능하면 방향 전환
                dir = (dir + 1) % 4;
            } else {
                // 이동 가능하면 위치 변경
                x = nx;
                y = ny;
            }
            k--;  // 1초 감소 (이동 또는 회전)
        }

        answer[0] = x;
        answer[1] = y;
        return answer;
    }

    public static void main(String[] args) {
        Solution2 T = new Solution2();
        int[][] arr1 = {
                {0, 0, 0, 0, 0},
                {0, 1, 1, 0, 0},
                {0, 0, 0, 0, 0},
                {1, 0, 1, 0, 1},
                {0, 0, 0, 0, 0}};
        System.out.println(Arrays.toString(T.solution(arr1, 10)));

        int[][] arr2 = {
                {0, 0, 0, 1, 0, 1},
                {0, 0, 0, 0, 0, 0},
                {0, 0, 0, 0, 0, 1},
                {1, 1, 0, 0, 1, 0},
                {0, 0, 0, 0, 0, 0},
                {0, 0, 0, 0, 0, 0}};
        System.out.println(Arrays.toString(T.solution(arr2, 20)));

        int[][] arr3 = {
                {0, 0, 1, 0, 0},
                {0, 1, 0, 0, 0},
                {0, 0, 0, 0, 0},
                {1, 0, 0, 0, 1},
                {0, 0, 0, 0, 0}};
        System.out.println(Arrays.toString(T.solution(arr3, 25)));
    }
}
