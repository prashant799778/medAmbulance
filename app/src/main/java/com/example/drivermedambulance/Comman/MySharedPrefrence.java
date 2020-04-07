package com.example.drivermedambulance.Comman;

import android.content.Context;
import android.content.SharedPreferences;

public class MySharedPrefrence {
    private static final String PREF_UNIQUE_ID = "PREF_UNIQUE_ID";
    private static final String PREFS_NAME = "sharedPreferences";

    static SharedPreferences sharedPreferences;
    static SharedPreferences.Editor prefEditor = null;
    private static Context mContext = null;
    public static MySharedPrefrence instance = null;

    public static MySharedPrefrence instanceOf(Context context) {
        mContext = context;
        if (instance == null) {
            instance = new MySharedPrefrence();
        }
        sharedPreferences = context.getSharedPreferences(PREFS_NAME, Context.MODE_PRIVATE);
        prefEditor = sharedPreferences.edit();
        return instance;
    }

    public void setLoggedIn(Boolean isLogIn) {
        prefEditor.putBoolean("login", isLogIn);
        prefEditor.commit();
    }

    public Boolean isLoggedIn() {
        return sharedPreferences.getBoolean("login", false);

    }


    public void setUserName(String userid) {
        prefEditor.putString("userid", userid);
        prefEditor.commit();
    }

    public String getUserName() {
        return sharedPreferences.getString("userid", "");

    }




    public void setAmbulanceId(String id) {
        prefEditor.putString("ambid", id);
        prefEditor.commit();
    }

    public String getAmbulanceId() {
        return sharedPreferences.getString("ambid", "");

    }




    public void setBookingId(String id) {
        prefEditor.putString("bookingid", id);
        prefEditor.commit();
    }

    public String getBookingId() {
        return sharedPreferences.getString("bookingid", "");

    }


    public void setDriverId(String id) {
        prefEditor.putString("driverid", id);
        prefEditor.commit();
    }

    public String getDriverId() {
        return sharedPreferences.getString("driverid", "");

    }



    public void setBookingUSerId(String id) {
        prefEditor.putString("setbid", id);
        prefEditor.commit();
    }

    public String getBookingUSerId() {
        return sharedPreferences.getString("setbid", "");

    }





    public void setBookingUSerMobile(String id) {
        prefEditor.putString("setbidm", id);
        prefEditor.commit();
    }

    public String getBookingUSerMobile() {
        return sharedPreferences.getString("setbidm", "");

    }



    public void setBookingUSerName(String name) {
        prefEditor.putString("usn", name);
        prefEditor.commit();
    }

    public String getBookingUSerName() {
        return sharedPreferences.getString("usn", "");

    }






    public void setUserId(String id) {
        prefEditor.putString("id", id);
        prefEditor.commit();
    }

    public String getUserId() {
        return sharedPreferences.getString("id", "");
    }

    public void setUserTypeId(String id) {

        prefEditor.putString("typeid", id);
        prefEditor.commit();
    }

    public String getUserProfile() {
        return sharedPreferences.getString("profile", "");
    }

    public void setUserProfile(String profile) {
        prefEditor.putString("profile", profile);
        prefEditor.commit();
    }
    public String getInterest() {
        return sharedPreferences.getString("interest", "");
    }

    public void setInterest(String interest) {
        prefEditor.putString("interest", interest);
        prefEditor.commit();
    }

    public String getUserTypeId() {
        return sharedPreferences.getString("typeid", "");
    }



    public String getUserEmail() {
        return sharedPreferences.getString("email", "");
    }

    public void setUserEmail(String email) {
        prefEditor.putString("email", email);
        prefEditor.commit();
    }


    public String getCountry() {
        return sharedPreferences.getString("country", "");
    }

    public void setCountry(String country) {
        prefEditor.putString("country", country);
        prefEditor.commit();
    }

    public String getcity() {
        return sharedPreferences.getString("city", "");
    }

    public void setcity(String country) {
        prefEditor.putString("city", country);
        prefEditor.commit();
    }
    public String getDescription() {
        return sharedPreferences.getString("dis", "");
    }

    public void setDescription(String dis) {
        prefEditor.putString("dis", dis);
        prefEditor.commit();
    }

    public String getUserPersonalAddress() {
        return sharedPreferences.getString("personalAddress", "");
    }

    public void setUserPersonalAddress(String personalAddress) {
        prefEditor.putString("personalAddress", personalAddress);
        prefEditor.commit();
    }




    public String getCompanyNAame() {
        return sharedPreferences.getString("cname", "");
    }

    public void setCompanyName(String cname) {
        prefEditor.putString("cname", cname);
        prefEditor.commit();
    }


    public String getMobile() {
        return sharedPreferences.getString("mobile", "");
    }

    public void setMobile(String mobile) {
        prefEditor.putString("mobile", mobile);
        prefEditor.commit();
    }





    public String getotp() {
        return sharedPreferences.getString("otp", "");
    }

    public void setotp(String mobile) {
        prefEditor.putString("otp", mobile);
        prefEditor.commit();
    }

    public String getAppVersion() {
        return sharedPreferences.getString("appVersion", "");
    }

    public void setAppVersion(String apVersion) {
        prefEditor.putString("appVersion", apVersion);
        prefEditor.commit();
    }

    public String getcurrentLocation() {
        return sharedPreferences.getString("currentLocation", "");
    }

    public void setcurrentLocation(String current) {
        prefEditor.putString("currentLocation", current);
        prefEditor.commit();
    }

    public String getcurrentLocationlatlong() {
        return sharedPreferences.getString("currentLocationlatlong", "");
    }

    public void setcurrentLocationlatlong(String currentlatlong) {
        prefEditor.putString("currentLocationlatlong", currentlatlong);
        prefEditor.commit();
    }

    public String getnotificationToken() {
        return sharedPreferences.getString("notificationToken", "");
    }

    public void setnotificationToken(String currentlatlong) {
        prefEditor.putString("notificationToken", currentlatlong);
        prefEditor.commit();
    }

    public String getdateCreate() {
        return sharedPreferences.getString("dateCreate", "");
    }

    public void setdateCreate(String currentlatlong) {
        prefEditor.putString("dateCreate", currentlatlong);
        prefEditor.commit();
    }

    public String getOrgatination() {
        return sharedPreferences.getString("org", "");
    }

    public void setOrganization(String org) {
        prefEditor.putString("org", org);
        prefEditor.commit();
    }


    public String getDasignation() {
        return sharedPreferences.getString("dsg", "");
    }

    public void setDasignation(String dsg) {
        prefEditor.putString("dsg", dsg);
        prefEditor.commit();
    }


    public String getname() {
        return sharedPreferences.getString("name", "Name");
    }

    public void setipAddress(String dsg) {
        prefEditor.putString("ipAddress", dsg);
        prefEditor.commit();
    }

    public String getipAddress() {
        return sharedPreferences.getString("ipAddress", "");
    }

    public void setname(String dsg) {
        prefEditor.putString("name", dsg);
        prefEditor.commit();
    }


    public String getProfileCategory() {
        return sharedPreferences.getString("c", "");
    }

    public void setProfileCategory(String c) {
        prefEditor.putString("c", c);
        prefEditor.commit();
    }

    public String getUniversityName() {
        return sharedPreferences.getString("un", "");
    }

    public void setUniversityName(String un) {
        prefEditor.putString("un", un);
        prefEditor.commit();
    }
    public String getUniversityAddress() {
        return sharedPreferences.getString("uadd", "");
    }

    public void setUniversityAddress(String uadd) {
        prefEditor.putString("uadd", uadd);
        prefEditor.commit();
    }


    public String getInstituteName() {
        return sharedPreferences.getString("ins", "");
    }

    public void setInstituteName(String ins) {
        prefEditor.putString("ins", ins);
        prefEditor.commit();
    }


    public String getQualification() {
        return sharedPreferences.getString("qu", "");
    }

    public void setQualication(String qu) {
        prefEditor.putString("qu", qu);
        prefEditor.commit();
    }


    public String getQualificationBatch() {
        return sharedPreferences.getString("bqu", "");
    }

    public void setQualicationBatch(String bqu) {
        prefEditor.putString("bqu", bqu);
        prefEditor.commit();
    }




    public void clearData() {
        prefEditor.clear();
        prefEditor.commit();
    }



}









