// 새로운 불면증 치료법(SWEA)

import java.io.BufferedReader;
import java.io.InputStreamReader;

public class solve002 {

    public static void main(String[] args) throws Exception {

        // 버퍼를 이용한 입출력: 속도 향상 목적
        // Enter 만 경계로 인식하고, 받은 데이터는 String 으로 고정되므로 데이터 가공 필요함!
        // 공백 단위 데이터 분할 필요하면 StringTokenizer 활용하기
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // testcase: 총 TC, total: bit 비교를 위한 변수(0 ~ 9 모두 나왔을 경우)
        int testcase = Integer.parseInt(br.readLine());
        int total = (1 << 10) - 1;

        for(int i = 1; i <= testcase ; i ++){
            // N: 주어진 숫자
            int N = Integer.parseInt(br.readLine());

            // visited: 본 숫자들을 담을 변수, count: 양 세기 몇번째?
            int visited = 0;
            int count = 0;

            for (count = 1;; count++) {
                // arr: 셀 양 마리수의 각 자리수를 char 로 변환한 array
                char[] arr = String.valueOf(N * count).toCharArray();

                // 각 자리수를 체크해서 visited 체크
                for (char c : arr) {
                    // ASCII code 활용해서 문자형 숫자를 숫자로 변환
                    int num = c - '0';

                    // 논리연산자 활용해서 visited 표시
                    visited = visited | (1 << num);
                }

                if (visited == total) break;
            }

        // Java 에서 %formatting 사용하려면 String.format 활용
        System.out.println(String.format("#%d %d", testcase, count * N));

        }
    }
}