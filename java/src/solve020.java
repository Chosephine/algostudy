
/*
 * programmers 코딩테스트 입문
 * 각도기
*/

public class solve020{
	
	public static int solution(int angle) {
        int answer = 0;
        
        if (angle == 90) {
        	answer = 2;
        } else if (angle == 180) {
        	answer = 4;
        } else if (angle > 0 && angle < 90) {
        	answer = 1;
        } else if (angle > 90 && angle < 180) {
        	answer = 3;
        }
        
        return answer;
    }
	
    public static void main(String[] args) throws Exception {
    	System.out.printf("hello world\n");
    	int inPut = 180;
//    	String eliminate = "f";
    	int answer = solution(inPut);
//    	ArrayList<Integer> answer = solution(inPut);
    	System.out.println(answer);
//    	System.out.println(answer);
    }
}
