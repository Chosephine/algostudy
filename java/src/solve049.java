

/*
 * 프로그래머스 120892 암호 해독 
*/

public class solve049 {
	public static String solution(String cipher, int code) {
		char[] charCipher = cipher.toCharArray();
        String answer = "";
        for (int i=0; i < cipher.length(); i++) {
        	if ( (i+1)%code == 0) {
        		answer += charCipher[i];
        	}
        }
        return answer;
    }
	public static void main(String[] args) {
		String cipher = "pfqallllabwaoclk";
		int code = 2;
		String answer = solution(cipher, code);
		System.out.println(answer);
	}
}
