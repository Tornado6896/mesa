	#ifndef _ANDROID_SYNC_H
	#define _ANDROID_SYNC_H

	#ifdef __cplusplus
	extern "C" {
	#endif

	int sync_wait(int fd, int timeout);
	int sync_merge(const char* name, int fd1, int fd2);

	#ifdef __cplusplus
	}
	#endif

	#endif	
