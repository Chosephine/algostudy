package src;
import java.util.*;

/*
 * 프로그래머스 120852 소인수분해 
*/

public class solve042 {
	public static Set<Integer> solution(int n) {
        Set<Integer> a = new TreeSet<Integer>();
        int target = n;
        while (!a.contains(target)) {
        	if (target == 1) break;
        	for (int i=2; i <= target; i++) {
        		if (target % i == 0) {
        			a.add(i);
        			target /= i;
        			break;
        			// 위 break	가 없으면 오답이 발생한다. 훔..
        		}
        	}
        }
        return a;
    }
	public static void main(String[] args) {
		int n = 583;
		Set<Integer> answer = solution(n);
		System.out.println(answer.toString());
	}
}
