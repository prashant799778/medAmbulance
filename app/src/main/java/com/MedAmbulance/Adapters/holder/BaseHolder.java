package com.MedAmbulance.Adapters.holder;

import android.view.View;
import androidx.recyclerview.widget.RecyclerView;
public abstract class BaseHolder extends RecyclerView.ViewHolder {
        private int mCurrentPosition;
        public BaseHolder(View itemView) {
            super(itemView);
        }
        protected abstract void clear();
        public void onBind(int position) {
            mCurrentPosition = position;
            clear();
        }
        public int getCurrentPosition() {
            return mCurrentPosition;
        }

    }
