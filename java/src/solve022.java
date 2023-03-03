
/*
 * programmers 코딩테스트 입문
 * 짝수의 합
*/

public class solve022{
	
	public static int solution(int n) {
        int answer = 0;
        for (int i = 1 ; i <= n ; i++ ) {
        	// i++ 대신 i+=2 도 가능!
        	if (i % 2 == 0) {
        		answer += i;
        	}
        }
        return answer;
    }
	
    public static void main(String[] args) throws Exception {
    	System.out.printf("hello world\n");
    	int inPut = 4;
    	int answer = solution(inPut);
//    	ArrayList<Integer> answer = solution(inPut);
    	System.out.println(answer);
//    	System.out.println(answer);
    }
}
