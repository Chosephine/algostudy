

/*
 * 프로그래머스 120851 숨어있는 숫자의 덧셈 (1)
*/

public class solve041 {
	public static int solution(String my_string) {
        int answer = 0;
        char[] my_chars = my_string.toCharArray();
        for (char c : my_chars) {
        	int target = c;
        	if (target >= 49 && target < 59) {
        		answer += (target - 48);
        	}
        }
        return answer;
    }
	public static void main(String[] args) {
		 String my_string = "1a2b3c4d123";
		 int answer = solution(my_string);
		 System.out.println(answer);
		 
		 // 1. Integer.parseInt() 메서드가 있다!
		 // 2. ASCII 사용할 꺼면 애초에 line 9~10 에서 직접 코드 넘버 입력하는 대
		 // '0'을 통해 알아서 변환 시켜도 좋았을지

	}
}
