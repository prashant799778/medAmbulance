package com.example.respondermedambulance.util;

import java.io.IOException;
import java.util.List;
import java.util.Locale;

import android.content.Context;
import android.location.Address;
import android.location.Geocoder;
import android.os.AsyncTask;
import android.util.Log;

public class GetLocationAsyncTask extends AsyncTask<String, Void, String> 
{
    // boolean duplicateResponse;
    double x, y;
    private StringBuilder str;
    private Context mContext;
    private Geocoder geocoder;
	private List<Address> addresses;

	/** The _listener. */
	private LocationReceivedListener listener = null;
    public GetLocationAsyncTask(Context context, double latitude, double longitude) 
    {
    	mContext = context;
        x = latitude;
        y = longitude;
    }

    @Override
    protected void onPreExecute() 
    {
//        Address.setText(" Getting location ");
    	Log.e("tag", "Getting location");
    }

    @Override
    protected String doInBackground(String... params) 
    {
        try {
            geocoder = new Geocoder(mContext, Locale.ENGLISH);
            addresses = geocoder.getFromLocation(x, y, 1);
            str = new StringBuilder();
            if (geocoder.isPresent()) 
            {
                Address returnAddress = addresses.get(0);

                String localityString = returnAddress.getLocality();
                String city = returnAddress.getCountryName();
                String region_code = returnAddress.getCountryCode();
                String zipcode = returnAddress.getPostalCode();

                str.append(localityString + "");
                str.append(city + "" + region_code + "");
                str.append(zipcode + "");

            } else 
            {
            	Log.e("tag", "Geocoder not present");
            }
        } catch (IOException e) {
            Log.e("tag", e.getMessage());
        }
        return null;

    }

    @Override
    protected void onPostExecute(String result) 
    {
        try 
        {
        	Address address = addresses.get(0);
        	if (null != listener && false == isCancelled()) 
    		{
    			listener.onAddressReceived(address);
    		}
    		else 
    		{
    			AppUtil.LogMsg("", "listener is null!!!");
    		}
//            Log.e("tag",
//            		"Line1:- "+ address.getAddressLine(0)+
//            		",\n Line2:- "+ address.getAddressLine(1) +
//            		",\n Admin Area:-"+ address.getAdminArea() + 
//            		",\n Locality:- "+ address.getLocality()+ 
//            		",\n Sub Locality:- "+ address.getSubLocality()+
//            		",\n Postal Code:-"+ address.getPostalCode()+
//            		",\n Country:-"+ address.getCountryName());
            
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    @Override
    protected void onProgressUpdate(Void... values) 
    {

    }
    
    /**
	 * Sets the listener.
	 * 
	 * @param listener
	 *            the new listener
	 */
	public void setListener(LocationReceivedListener listener) 
	{
		this.listener = listener;
	}
    
    public interface LocationReceivedListener 
	{
		public void onAddressReceived(Address address);
	}
}