

/*
 * 프로그래머스 120902 문자열 계산하기
*/

public class solve056 {
	public static int solution(String my_string) {
		// my_string을 계산한 (중간)결과값은 -100,000 ~ 100,000 이므로 int 자료형 사용
        int answer = 0;
        
        String[] tokens = my_string.split(" ");
        
        // operator이 true일 때 덧셈연산,
        // false일 때 뺄셈 연산
        boolean operator = true;
        
        // token을 순회하면서 숫자면 계산, 연산자면 operator 변경
        for (String token : tokens) {
        	if (token.equals("+")) {
        		operator = true;
        	} else if (token.equals("-")) {
        		operator = false;
        	} else {
	        		if (operator) {answer += Integer.parseInt(token);}
	        		else {answer -= Integer.parseInt(token);}
        		}
        	}
        
        return answer;
    }
	
	public static void main(String[] args) {
		
		String input_case = "3 + 4";
		
		System.out.println(solution(input_case));
	}
}
