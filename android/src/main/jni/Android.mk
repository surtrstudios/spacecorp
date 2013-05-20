LOCAL_PATH := $(call my-dir)

include $(CLEAR_VARS)

LOCAL_MODULE      := spacecorp
LOCAL_SRC_FILES   := main.c
LOCAL_LDLIBS   := -landroid
LOCAL_STATIC_LIBRARIES := android_native_app_glue 
LOCAL_CFLAGS += -DSURTR_PLATFORM_ANDROID

include $(BUILD_SHARED_LIBRARY)

$(call import-module,android/native_app_glue)