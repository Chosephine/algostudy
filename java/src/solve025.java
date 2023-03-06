import java.util.*;

/*
 * programmers 코딩테스트 입문
 * 진료 순서 정하기
*/

public class solve025{
	
	public static int[] solution(int[] emergency) {
		int[] original = Arrays.copyOf(emergency, emergency.length);
		Arrays.sort(emergency);
		System.out.println("emergency : " + Arrays.toString(emergency));
		System.out.println("original : " + Arrays.toString(original));
        int[] answer = new int[emergency.length];
        for (int i = 0 ; i < emergency.length ; i++) { 
        	// emergency 순서대로 순회해서 answer에 역순으로 추가
        	for (int j = 0 ; j < emergency.length ; j++) {
        		if (emergency[i] == original[j]) {        			
        			answer[j] =  emergency.length - i;
        			break;
        		}
        	}
        }
        return answer;
    }
	
    public static void main(String[] args) throws Exception {
    	System.out.printf("hello world\n");
    	int[] inPut = {30, 10, 23, 6, 100};
//    	int inPut2 = 3;
    	int[] answer = solution(inPut);
//    	ArrayList<Integer> answer = solution(inPut);
    	System.out.println(Arrays.toString(answer));
//    	System.out.println(answer);
    }
}
