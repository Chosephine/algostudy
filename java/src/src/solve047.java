package src;

/*
 * 프로그래머스 120890 가까운 수 
*/

public class solve047 {
	public static int solution(int[] array, int n) {
		int answer = 101;
		int dif = 101;
		for(int a : array) {
			if ( Math.abs(a-n) < dif ) {
					answer = a;
					dif = Math.abs((a-n));
			} else if (Math.abs(a-n) == dif) {
				if (a < answer) {
					answer = a;
					dif = Math.abs((a-n));
				}
			}
		}
        return answer;
    }
	public static void main(String[] args) {
		int[] array = {3, 10, 28, 12};
		int n = 20;
		int answer = solution(array, n);
		System.out.println(answer);
	}
}
