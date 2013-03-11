#include <stdio.h>
#include "ffiprimes.h"

void primes(int results[10]) {
	int k, n, i, kmax;
	int p[10] = {0,0,0,0,0,0,0,0,0,0};
	kmax = 10;
	k = 0;
	n = 2;
	while (k < kmax) {
		i = 0;
		while ( (i < k) && ((n % p[i]) != 0) ) {
			i = i+1;
		}
		if (i == k) {
			p[k] = n;
			results[k] = n;
			k = k + 1;
		}
		n = n+1;
	}
}

int main() {
	int a[10] = {0,0,0,0,0,0,0,0,0,0};
	primes(a);
	int i;
	for (i=0;i<10;++i){
		printf("%d ",a[i]);
	}
	printf("\n");
}
