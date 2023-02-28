import java.util.Arrays;

/*
 * programmers 코딩테스트 입문
 * 아이스 아메리카노
*/

public class solve013{
	
	public static int[] solution(int money) {
        int[] answer = new int[2];
        answer[0] = money / 5500;
        answer[1] = money - 5500 * answer[0];
        return answer;
    }

    public static void main(String[] args) throws Exception {
    	System.out.printf("hello world\n");
    	int inPut = 15000;
//    	int people = 12;
    	int[] answer = solution(inPut);
//    	ArrayList<Integer> answer = solution(inPut);
    	System.out.println(Arrays.toString(answer));
//    	System.out.println(answer);
    }
}
