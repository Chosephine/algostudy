package src;

/*
 * 프로그래머스 120898 편지
*/

public class solve053 {
	public static int solution(String message) {
        char[] charMessage = message.toCharArray();
        int answer = charMessage.length * 2;
        return answer;
    }
	
	public static void main(String[] args) {
		String msg1 = "happy birthday!"	;
		int answer = solution(msg1);
		System.out.println(answer);
	}
}
