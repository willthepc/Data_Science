#Amostra 1
zScorePri = (amostra1['Preço.Final'] - amostra1['Preço.Final'].mean()) / amostra1['Preço.Final'].std(ddof=0)
zPri_mean = zScorePri.abs().mean()

q1Pri = amostra1['Preço.Final'].quantile(0.25)
q3Pri = amostra1['Preço.Final'].quantile(0.75)
iqrPri = q3Pri - q1Pri

limite_inf_pri = q1Pri - 1.5 * iqrPri
limite_sup_pri = q3Pri + 1.5 * iqrPri

amostra1['Outlier_IQR'] = (amostra1['Preço.Final'] < limite_inf_pri) | (amostra1['Preço.Final'] > limite_sup_pri)
amostra1['Outlier_Zscore'] = zScorePri.abs() > 3

iqrPri = pd.DataFrame({
    "IQR": [iqrPri],
    "zScore": [zPri_mean],
    "Outliers IQR": [len(amostra1[amostra1['Outlier_IQR'] == True])],
    "Outliers Zscore": [len(amostra1[amostra1['Outlier_Zscore'] == True])]
})

# Amostra 2
zScoreSeg = (amostra2['Preço.Final'] - amostra2['Preço.Final'].mean()) / amostra2['Preço.Final'].std(ddof=0)
zSeg_mean = zScoreSeg.abs().mean()

q1Seg = amostra2['Preço.Final'].quantile(0.25)
q3Seg = amostra2['Preço.Final'].quantile(0.75)
iqrSeg = q3Seg - q1Seg

limite_inf_seg = q1Seg - 1.5 * iqrSeg
limite_sup_seg = q3Seg + 1.5 * iqrSeg

amostra2['Outlier_IQR'] = (amostra2['Preço.Final'] < limite_inf_seg) | (amostra2['Preço.Final'] > limite_sup_seg)
amostra2['Outlier_Zscore'] = zScoreSeg.abs() > 3

iqrSeg = pd.DataFrame({
    "IQR": [iqrSeg],
    "zScore": [zSeg_mean],
    "Outliers IQR": [len(amostra2[amostra2['Outlier_IQR'] == True])],
    "Outliers Zscore": [len(amostra2[amostra2['Outlier_Zscore'] == True])]
})


#Original
zScoreOr =  (df['Preço.Final'] - df['Preço.Final'].mean()) / df['Preço.Final'].std(ddof=0)
zOr_mean  = zScoreOr.abs().mean()

q1Or = df['Preço.Final'].quantile(0.25)
q3Or = df['Preço.Final'].quantile(0.75)
iqrOr = q3Or - q1Or

limite_inf_or = q1Or - 1.5 * iqrOr
limite_sup_or = q3Or + 1.5 * iqrOr

df['Outlier_IQR'] = (df['Preço.Final'] < limite_inf_or) | (df['Preço.Final'] > limite_sup_or)
df['Outlier_Zscore'] = zScoreOr.abs() > 3

iqrOr = pd.DataFrame({
    "IQR": [iqrOr],
    "zScore": [zOr_mean],
    "Outliers IQR": [len(df[df['Outlier_IQR'] == True])],
    "Outliers Zscore": [len(df[df['Outlier_Zscore'] == True])]
})

#tabela

tabela_IQR = pd.concat([iqrPri, iqrSeg, iqrOr], axis=0)

tabela_IQR.index = ["Amostra 1", "Amostra 2", "População Geral"]

tabela_IQR