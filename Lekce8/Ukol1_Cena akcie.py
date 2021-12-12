# Pomocí modulu yfinance, který jsme používali v 5. lekci, stáhni ceny akcií společnosti Cisco (používají "Ticker" CSCO) za posledních 5 let.
# Dále pracuj s cenami akcie v závěru obchodního dne, tj. použij sloupec "Close".

import yfinance as yf
from statsmodels.graphics.tsaplots import plot_acf
import matplotlib.pyplot as plt
from statsmodels.tsa.ar_model import AutoReg
from statsmodels.graphics.tsaplots import plot_acf
import  pandas

csco = yf.Ticker("CSCO")
csco_df = csco.history(period="5y")
print(csco_df)

# Zobraz si graf autokorelace a podívej se, jak je hodnota ceny závislná na svých vlastních hodnotách v minulosti.

csco_df["Close"].autocorr(lag=1)

plot_acf(csco_df["Close"])
plt.show()


# Zkus použít AR model k predikci cen akcie na příštích 5 dní.

csco_df_50=csco_df.tail(50)
model=AutoReg(csco_df_50["Close"], lags=5, seasonal=True, period=12)
model_fit=model.fit()


# Zobraz v grafu historické hodnoty (nikoli celou řadu, ale pro přehlednost např. hodnoty za posledních 50 dní) a tebou vypočítanou predikci.
predictions = model_fit.predict(start=csco_df_50.shape[0], end=csco_df_50.shape[0] + 5)
df_forecast = pandas.DataFrame(predictions, columns=["Prediction"])
df_with_prediction = pandas.concat([csco_df_50, df_forecast])
df_with_prediction[["Close", "Prediction"]].plot()
plt.show()