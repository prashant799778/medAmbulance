package com.MedAmbulance.util;

import java.io.ByteArrayOutputStream;
import java.io.File;
import java.io.FileOutputStream;
import java.io.FileWriter;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStreamWriter;
import java.io.PrintWriter;
import java.io.StringWriter;
import java.io.Writer;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;

import android.Manifest;
import android.annotation.SuppressLint;
import android.app.Activity;
import android.content.Context;
import android.content.DialogInterface;
import android.content.Intent;
import android.content.pm.PackageInfo;
import android.content.pm.PackageManager;
import android.content.pm.PackageManager.NameNotFoundException;
import android.content.res.Resources;
import android.content.res.TypedArray;
import android.graphics.Bitmap;
import android.graphics.Bitmap.CompressFormat;
import android.graphics.Typeface;
import android.provider.Settings;
import android.telephony.TelephonyManager;
import android.util.AttributeSet;
import android.util.Base64;
import android.util.Log;
import android.util.TypedValue;
import android.view.View;
import android.view.inputmethod.InputMethodManager;
import android.widget.TextView;
import android.widget.Toast;

import com.MedAmbulance.R;

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;

public class AppUtil {
	/** The typeface cache. */
	public static Map<String, Typeface> typefaceCache = new HashMap<String, Typeface>();

	/**
	 * Sets the typeface.
	 *
	 * @param attrs
	 *            the attrs
	 * @param textView
	 *            the text view
	 */
	@SuppressLint("StringFormatInvalid")
	public static void setTypeface(AttributeSet attrs, TextView textView) {
		Context context = textView.getContext();
		TypedArray values = context.obtainStyledAttributes(attrs, R.styleable.CustomTextView);
		String typefaceName = values.getString(R.styleable.CustomTextView_typeface);

		if (typefaceCache.containsKey(typefaceName)) {
			textView.setTypeface(typefaceCache.get(typefaceName));
		} else {
			Typeface typeface;
			try {
				typeface = Typeface.createFromAsset(textView.getContext().getAssets(), context.getString(R.string.assets_fonts_folder) + typefaceName);
			} catch (Exception e) {
				Log.v(context.getString(R.string.app_name), String.format(context.getString(R.string.typeface_not_found), typefaceName));
				return;
			}

			typefaceCache.put(typefaceName, typeface);
			textView.setTypeface(typeface);
		}

		values.recycle();
	}


	/**
	 * Log msg.
	 *
	 * @param tag
	 *            the tag
	 * @param msg
	 *            the msg
	 */
	public static void LogMsg(String tag, String msg) {
		Log.e(tag, msg);
		if (AppConstants._isLoggingEnabled == true) {
			if (AppConstants._isFileLoggingEnabled) {
				Log.e(tag, msg);
				writeToFile(AppConstants.LOG_FILENAME, tag + ":" + msg + "\n");
			}
		}
	}


	/**
	 * Write to file.
	 *
	 * @param fileName
	 *            the file name
	 * @param content
	 *            the content
	 */
	public static void writeToFile(String fileName, String content) {
		try {
			FileWriter fw = new FileWriter(fileName, true);
			fw.write(content);

			fw.flush();
			fw.close();
		} catch (IOException ex) {
			ex.printStackTrace();
			AppUtil.LogException(ex);
		}
	}

	/**
	 * Log error.
	 *
	 * @param tag
	 *            the tag
	 * @param msg
	 *            the msg
	 */
	public static void LogError(String tag, String msg) {
		if (AppConstants._isLoggingEnabled == true) {
			if (AppConstants._isFileLoggingEnabled) {
				Log.e(tag, msg);
				writeToFile(AppConstants.LOG_FILENAME, tag + ":" + msg + "\n");
			}
		}
	}


	/**
	 * Log exception.
	 *
	 * @param ex the ex
	 */
	public static void LogException(Throwable ex) {
		if (true == AppConstants._isFileExceptionLoggingEnabled == true) {
			final Writer writer = new StringWriter();
			final PrintWriter printWriter = new PrintWriter(writer);

			ex.printStackTrace(printWriter);
			String stackTrace = writer.toString();
			printWriter.close();

			AppUtil.writeToFile(AppConstants.LOG_FILENAME, stackTrace);
		}
	}

	public static void StartActivityWithAnimation(Activity activity, Intent intent) {
		activity.startActivity(intent);
		activity.overridePendingTransition(R.anim.slide_in_right, R.anim.slide_out_left);
	}


	/**
	 * Gets the custom gson.
	 *
	 * @return the custom gson
	 */
	public static Gson getCustomGson() {
//		GsonBuilder gb = new GsonBuilder();
//		gb.registerTypeAdapter(UserType.class, new UserTypeSerializerDeserializer());
//		return gb.create();
		return null;
	}

	/**
	 * Gets the bytes from bitmap.
	 *
	 * @param bitmap the bitmap
	 * @return the bytes from bitmap
	 */
	public static byte[] getBytesFromBitmap(Bitmap bitmap) {
		if (null != bitmap) {
			ByteArrayOutputStream stream = new ByteArrayOutputStream();
			bitmap.compress(CompressFormat.JPEG, 100, stream);
			return stream.toByteArray();
		}

		return null;
	}

	/**
	 * Gets the base64 string.
	 *
	 * @param bitmap the bitmap
	 * @return the base64 string
	 */
	public static String getBase64String(Bitmap bitmap) {
		return Base64.encodeToString(getBytesFromBitmap(bitmap), Base64.NO_WRAP);
	}

	/**
	 * Gets the device id.
	 *
	 * @param context
	 *            the context
	 * @return the device id
	 */
	public static String getDeviceID(Context context) {
//		TelephonyManager telephonyManager = (TelephonyManager) context.getSystemService(Context.TELEPHONY_SERVICE);
//
//		String deviceID = telephonyManager.getDeviceId();
//
//		if (null == deviceID || 0 >= deviceID.length()) {
//			deviceID = android.os.Build.SERIAL;
//		}
//
//		if (null == deviceID || 0 >= deviceID.length()) {
//			deviceID = Settings.Secure.ANDROID_ID;
//		}

		return "";
	}
	
	
	public static void showToastMsg(String msg, Context ctx) 
	{
		Toast.makeText(ctx, msg, Toast.LENGTH_LONG).show();
	}
	
	
	public static void writeFileToSdCard(String data)
	{
		try {
			File myFile = new File(AppConstants.LOG_FILENAME);
			myFile.createNewFile();
			FileOutputStream fOut = new FileOutputStream(myFile);
			OutputStreamWriter myOutWriter = new OutputStreamWriter(fOut);
			myOutWriter.append(data);
			myOutWriter.close();
			fOut.close();
		} catch (Exception e) {
			e.printStackTrace();
		}
	}
	
	
	
	/**
	 * Load json from asset.
	 * 
	 * @param context
	 *            the context
	 * @param jsonFileName
	 *            the json file name
	 * @return the string
	 */
	public static String loadJSONFromAsset(Context context, String jsonFileName) {
		String json = null;
		try {
			InputStream is = context.getAssets().open(jsonFileName);
			int size = is.available();

			byte[] buffer = new byte[size];
			is.read(buffer);
			is.close();

			json = new String(buffer, "UTF-8");
		}
		catch (IOException ex) {
			ex.printStackTrace();
			AppUtil.LogException(ex);
			return null;
		}
		return json;
	}
	
	
	public static int dpToPx(Context context, int dp) {
        float density = context.getResources().getDisplayMetrics().density;
        return Math.round((float) dp * density);
    }
	
	
	public static int dpToPx(Resources res, int dp) {
		return (int) TypedValue.applyDimension(TypedValue.COMPLEX_UNIT_DIP, dp, res.getDisplayMetrics());
	}
	
	
	public static void hideSoftKeyboard(Activity activity) 
	{
		InputMethodManager inputMethodManager = (InputMethodManager) activity
				.getSystemService(Activity.INPUT_METHOD_SERVICE);
		 if(inputMethodManager.isActive()){
		System.out.println("Keyboard hiden");
		inputMethodManager.hideSoftInputFromWindow(activity.getCurrentFocus()
				.getWindowToken(), 0);
		 } else {
		 System.out.println("Keyboard not visible");
		 }
	}
	
	public static void showInternetToast(Context ctx)
	{
		AppUtil.showToastMsg("no internet Connection", ctx);
	}
	
	/**
	 * Gets the application version.
	 * 
	 * @param context
	 *            the context
	 * @return the application version
	 */
	public static String getApplicationVersion(Context context) {
		String appVersion = "1.0";

		PackageInfo pInfo = null;
		try {
			pInfo = context.getPackageManager().getPackageInfo(context.getPackageName(), 0);
			appVersion = pInfo.versionName;
		}
		catch (NameNotFoundException ex) {
			ex.printStackTrace();
			AppUtil.LogException(ex);
		}
		return appVersion;
	}

	/**
	 * Gets the application version code.
	 * 
	 * @param context the context
	 * @return the application version code
	 */
	public static int getApplicationVersionCode(Context context) {
		int appVersionCode = 0;

		PackageInfo pInfo = null;
		try {
			pInfo = context.getPackageManager().getPackageInfo(context.getPackageName(), 0);
			appVersionCode = pInfo.versionCode;
		}
		catch (NameNotFoundException ex) {
			ex.printStackTrace();
			AppUtil.LogException(ex);
		}
		return appVersionCode;
	}

	
	public static void showNoInternetPopup(Context ctx) 
	{
//		final MaterialDialog alertDialog = new MaterialDialog(ctx);
//		alertDialog.setTitle(ctx.getResources().getString(R.string.error));
//		// Setting Dialog Message
//		alertDialog.setMessage(ctx.getResources().getString(R.string.prompt_no_internet));
//		alertDialog.setPositiveButton(
//				ctx.getResources().getString(R.string.ok), new View.OnClickListener() {
//                    @Override
//                    public void onClick(View v)
//                    {
//                    	alertDialog.dismiss();
//                    }
//                }
//            )
//            .setCanceledOnTouchOutside(false)
//            .setOnDismissListener(
//                new DialogInterface.OnDismissListener() {
//                    @Override
//                    public void onDismiss(DialogInterface dialog)
//                    {
//
//                    }
//                }
//            )
//            .show();
	}
	
	
	public static void shareText(Context ctx, String textToShare)
	{
		Intent sendIntent = new Intent();
		sendIntent.setAction(Intent.ACTION_SEND);
		sendIntent.putExtra(Intent.EXTRA_TEXT, textToShare);
		sendIntent.setType("text/plain");
		ctx.startActivity(sendIntent);
	}
	
	public static String generateAppShareText(Context context)
	{
		return context.getResources().getString(R.string.invite_default_msg) +" "+AppConstants.TLT_PLAYSTORE_WEB_URL;
	}
	
	

}
