package com.MedAmbulance.util;

import android.os.Environment;

/*
 * The Class AppConstants.
 * 
 */

public class AppConstants 
{
	public static final String COGNALYS_APPID = "3f08f9c308974a85a17d5fa";
	
	public static final String COGNALYS_ACCESS_TOKEN ="10f87a0bd9b433110bf18108688424bee4f48a0c";
	
	/** The Constant SUCCESS. */
	public static final int SUCCESS = 0;

	/** The Constant FAILURE. */
	public static final int FAILURE = 0;

	/** The Constant SECOND. 1000 mili-second */
	public static final long SECOND = 1000L;

	/** The Constant MIN. */
	public static final long MINUTE = 60L * SECOND;

	/** The Constant HOUR. */
	public static final long HOUR = 60L * MINUTE;

	/** The Constant MINIMUM_PASSWORD_LENGTH. */
	public static int MINIMUM_PASSWORD_LENGTH = 5;

	/** The Constant MAXIMUM_PASSWORD_LENGTH. */
	public static int MAXIMUM_PASSWORD_LENGTH = 15;

	/****************Basant***********************/
	public static final String SERVICE_SERVER_ADDRESS = "http://54.175.114.51/tribe/index.php/api/tlt";
	
	public static final String API_KEY = "abcdefghijklmnopqrstuvwxyzabcdefghijklmn";
	
	/** The Constant SERVICE_METHOD_init. */
	public final static String SERVICE_METHOD_init = "init";
	
	/** The Constant SERVICE_METHOD_Signup. */
	public final static String SERVICE_METHOD_Signup = "signup";
	
	/** The Constant SERVICE_METHOD_getOtp. */
	public final static String SERVICE_METHOD_getOtp= "mobile";
	
	/** The Constant SERVICE_METHOD_verifyOtp. */
	public final static String SERVICE_METHOD_verifyOtp= "otp";
	
	/** The Constant SERVICE_METHOD_PhonebookSync. */
	public final static String SERVICE_METHOD_PhonebookSync="contactlist";
	
	
	
	/** The Constant SERVICE_METHOD_Login. */
	public final static String SERVICE_METHOD_Login = "login";
	
	/** The Constant SERVICE_METHOD_UpdateProfile. */
	public final static String SERVICE_METHOD_UpdateProfile = "update";
	
	/** The Constant SERVICE_METHOD_AddSkill. */
	public final static String SERVICE_METHOD_AddSkill = "moderator";
	
	/** The Constant SERVICE_METHOD_GETSKILLS. */
	public final static String SERVICE_METHOD_GETSKILLS = "listSkills";
	
	/** The Constant SERVICE_METHOD_SEARCH. */
	public final static String SERVICE_METHOD_SEARCH = "searchResult";
	
	
	
	/** The Constant LOG_FILENAME. */
	public static final String LOG_FILENAME = Environment.getExternalStorageDirectory().getAbsolutePath() + "/TLTlogfile.txt";
	
	/** The Constant APP_SHARED_PREF_NAME. */
	public static final String APP_SHARED_PREF_NAME = "thelocaltribe";

	/** The Constant GENERIC_DIALOG_TAG. */
	public static final String GENERIC_DIALOG_TAG = "FragmentDialog";


	/** The Constant ASSET_JSON_FILENAME. */
	public static final String ASSET_JSON_FILENAME = "testJson.json";

	/** The Constant MB. */
	public static final int MB = 1 * 1024 * 1024;

	/** The Constant MAX_BITMAP_CACHE_SIZE. */
	public static final int MAX_MEMORY_CACHE_SIZE = 4 * MB;

	/** The Constant MAX_DISK_CACHE_SIZE. */
	public static final int MAX_DISK_CACHE_SIZE = 50 * MB;
	
	/** The _is logging enabled. */
	public static boolean _isLoggingEnabled = false;

	/** The _is file logging enabled. */
	public static boolean _isFileLoggingEnabled = false;

	/** The _is exception logging enabled. */
	public static boolean _isFileExceptionLoggingEnabled = false;
	
	public static final String SP_KEY_USER_DETAIL = "userinfo";
	
	public static final String SP_KEY_SKILL_STATUS = "skill_status";
	public static final String SP_KEY_SERVICEAREA_STATUS = "servicearea_status";
	public static final String SP_KEY_SERVICEAREA_ONLINE_STATUS = "servicearea_online_status";
	public static final String SP_KEY_SERVICEAREA_WORKPLACE_STATUS = "servicearea_workplace_status";
	public static final String SP_KEY_SERVICEAREA_HOME_STATUS = "servicearea_home_status";
	public static final String SP_KEY_VERIFICATION_STATUS = "verification_status";
	public static final String SP_KEY_AVAILABILITY_STATUS = "availability_status";
	public static final String SP_KEY_RATECARD_STATUS = "ratecard_status";
	public static final String SP_KEY_BANKDETAIL_STATUS = "bankdetail_status";
	public static final String SP_KEY_OTP = "tltotp";
	
	public static final int TAG_HOME_ADDRESS = 1;
	
	public static final int TAG_SKILL_NEXT = 2;
	public static final int TAG_RATECARD_NEXT = 3;
	
	public static final int TAG_ADDRESS_BACK = 4;
	public static final int TAG_AVAILABILITY_NEXT = 5;
	
	public static final int VERIFICATION_TYPE_SMS_PUSH = 1001;
	public static final int VERIFICATION_TYPE_P2P = 1002;
	public static final int VERIFICATION_TYPE_MISSED_CALL = 1003;
	
	/************ The Constant TLT_PLAYSTORE_WEB_URL. ***********/
	public static final String TLT_PLAYSTORE_WEB_URL = "https://play.google.com/store/apps/details?id=com.thelocaltribe";
	
}
