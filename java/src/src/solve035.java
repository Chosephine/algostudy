package src;

/*
 * 주사위의 개수
*/

public class solve035 {
	public static int solution(int[] box, int n) {
		// box = {상자의 가로, 세로, 높이}
		// n = 주사위 모서리 길이 정
        int answer = (box[0]/n) * (box[1]/n) * (box[2]/n) ;
        return answer;
    }
	public static void main(String[] args) {
		int[] box = {10, 8, 6};
		int n = 3;
		int answer = solution(box, n);
		System.out.println(answer);
	}
}
