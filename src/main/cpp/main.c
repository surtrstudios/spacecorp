#include <stdio.h>

int main(void)
{
#ifdef SURTR_PLATFORM_ANDROID
	printf("Hello Android\n");
#else
	printf("Hello\n");
#endif
} 