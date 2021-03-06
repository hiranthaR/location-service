package lk.eclk.locationservice.data.remote

import android.content.Context
import android.net.ConnectivityManager
import lk.eclk.locationservice.data.remote.ConnectivityInterceptor
import lk.eclk.locationservice.internal.NoConnectivityException
import okhttp3.Interceptor
import okhttp3.Response

class ConnectivityInterceptorImpl(context: Context) :
    ConnectivityInterceptor {
    private val appContext = context.applicationContext
    override fun intercept(chain: Interceptor.Chain): Response {
        if (!isOnline()) throw NoConnectivityException()
        return chain.proceed(chain.request())
    }

    private fun isOnline(): Boolean {
        val connectivityManger =
            appContext.getSystemService(Context.CONNECTIVITY_SERVICE) as ConnectivityManager
        val networkInfo = connectivityManger.activeNetworkInfo
        return networkInfo != null && networkInfo.isConnected
    }
}