package com.example.respondermedambulance.Activity;


import android.graphics.drawable.ColorDrawable;
import android.os.Bundle;

import androidx.appcompat.app.AppCompatActivity;

import com.example.respondermedambulance.Widget.CustomProgressDialog;


// TODO: Auto-generated Javadoc
/**
 * The Class PlashBaseActivity.
 */
public class TLTBaseActivity extends AppCompatActivity {

    /** The _is app went to bg. */
    private boolean _isAppWentToBg = false;

    protected CustomProgressDialog _progressDialog = null;

    /*
     * (non-Javadoc)
     *
     * @see android.app.Activity#onPause()
     */
    @Override
    protected void onPause() {
        super.onPause();
    }

    /*
     * (non-Javadoc)
     *
     * @see android.app.Activity#onResume()
     */
    @Override
    protected void onResume() {
        super.onResume();
		/*Settings.publishInstallAsync(getApplicationContext(), getString(R.string.app_id));
		PlashNewsApplication.getAppInstance().setIsAppInBackground(false);*/

        if (true == _isAppWentToBg)
        {
            _isAppWentToBg = false;
        }
    }

    /*
     * (non-Javadoc)
     *
     * @see android.app.Activity#onCreate(android.os.Bundle)
     */
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

    }

    /**
     * Show progress dialog.
     *
     * @param message
     *            the message
     */
    protected void showProgressDialog(int message) {
        _progressDialog = new CustomProgressDialog(this, getResources().getString(message));
        _progressDialog.getWindow().setBackgroundDrawable(new ColorDrawable(android.graphics.Color.TRANSPARENT));
        _progressDialog.setCancelable(false);
        if (null != _progressDialog) {
            _progressDialog.setMessage(getResources().getString(message));
            _progressDialog.show();
        }
    }

    /**
     * Show progress dialog.
     *
     * @param title
     *            the title
     * @param message
     *            the message
     */
    protected void showProgressDialog(int title, int message)
    {
        if (null != _progressDialog)
        {
            _progressDialog.setTitle(title);
            _progressDialog.setMessage(getResources().getString(message));
            _progressDialog.show();
        }
    }

    /**
     * Show progress dialog.
     *
     * @param messageText
     *            the message text
     */
    protected void showProgressDialog(String messageText) {
        if (null != _progressDialog) {
            _progressDialog.setMessage(messageText);
            _progressDialog.show();
        }
    }

    /**
     * Hide progress dialog.
     *
     */
    protected void hideProgressDialog() {
        if (null != _progressDialog && _progressDialog.isShowing()) {
            _progressDialog.dismiss();
        }
    }



    /*
     * (non-Javadoc)
     *
     * @see android.app.Activity#onDestroy()
     */
    @Override
    protected void onDestroy() {
        super.onDestroy();

    }

    /*
     * (non-Javadoc)
     *
     * @see android.app.Activity#onStart()
     */
    @Override
    protected void onStart() {
        super.onStart();
    }

    /*
     * (non-Javadoc)
     *
     * @see android.app.Activity#onStop()
     */
    @Override
    protected void onStop() {
        super.onStop();
    }


    /*
     * (non-Javadoc)
     *
     * @see
     * com.slidingmenu.lib.app.SlidingFragmentActivity#onSaveInstanceState(android
     * .os.Bundle)
     */
    @Override
    protected void onSaveInstanceState(Bundle outState) {
        super.onSaveInstanceState(outState);

    }
}
