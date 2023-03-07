# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class TestInstances(models.Model):
    input_id = models.IntegerField(primary_key=True)
    unit_number = models.BigIntegerField(blank=True, null=True)
    rul = models.BigIntegerField(db_column='RUL', blank=True, null=True)  # Field name made lowercase.
    s_2 = models.FloatField(blank=True, null=True)
    s_3 = models.FloatField(blank=True, null=True)
    s_4 = models.FloatField(blank=True, null=True)
    s_7 = models.FloatField(blank=True, null=True)
    s_8 = models.FloatField(blank=True, null=True)
    s_9 = models.FloatField(blank=True, null=True)
    s_11 = models.FloatField(blank=True, null=True)
    s_12 = models.FloatField(blank=True, null=True)
    s_13 = models.FloatField(blank=True, null=True)
    s_14 = models.FloatField(blank=True, null=True)
    s_15 = models.FloatField(blank=True, null=True)
    s_17 = models.FloatField(blank=True, null=True)
    s_20 = models.FloatField(blank=True, null=True)
    s_21 = models.FloatField(blank=True, null=True)
    rf_loss = models.FloatField(db_column='RF_loss', blank=True, null=True)  # Field name made lowercase.
    svr_loss = models.FloatField(db_column='SVR_loss', blank=True, null=True)  # Field name made lowercase.
    xgb_loss = models.FloatField(db_column='XGB_loss', blank=True, null=True)  # Field name made lowercase.
    lgb_loss = models.FloatField(db_column='LGB_loss', blank=True, null=True)  # Field name made lowercase.
    bayes_loss = models.BigIntegerField(db_column='BAYES_loss', blank=True, null=True)  # Field name made lowercase.
    rs_loss = models.FloatField(db_column='RS_loss', blank=True, null=True)  # Field name made lowercase.
    lr_loss = models.FloatField(db_column='LR_loss', blank=True, null=True)  # Field name made lowercase.
    mlp_loss = models.FloatField(db_column='MLP_loss', blank=True, null=True)  # Field name made lowercase.
    mlp1_loss = models.FloatField(db_column='MLP1_loss', blank=True, null=True)  # Field name made lowercase.
    lstm_loss = models.FloatField(db_column='LSTM_loss', blank=True, null=True)  # Field name made lowercase.
    cnn_loss = models.FloatField(db_column='CNN_loss', blank=True, null=True)  # Field name made lowercase.
    cnn1_loss = models.FloatField(db_column='CNN1_loss', blank=True, null=True)  # Field name made lowercase.
    gru_loss = models.FloatField(db_column='GRU_loss', blank=True, null=True)  # Field name made lowercase.
    lstm1_loss = models.FloatField(db_column='LSTM1_loss', blank=True, null=True)  # Field name made lowercase.
    umap_x = models.FloatField(blank=True, null=True)
    umap_y = models.FloatField(blank=True, null=True)
    pca_x = models.FloatField(blank=True, null=True)
    pca_y = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'test_instances'


class TestUnitPca(models.Model):
    unit_number = models.BigIntegerField(primary_key=True)
    umap_x = models.FloatField(blank=True, null=True)
    umap_y = models.FloatField(blank=True, null=True)
    pca_x = models.FloatField(blank=True, null=True)
    pca_y = models.FloatField(blank=True, null=True)
    rul = models.BigIntegerField(db_column='RUL', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'test_unit_pca'


class ShapValue(models.Model):
    input_id = models.BigIntegerField(primary_key=True)
    cnn1_s_2 = models.FloatField(db_column='CNN1_s_2', blank=True, null=True)  # Field name made lowercase.
    cnn1_s_3 = models.FloatField(db_column='CNN1_s_3', blank=True, null=True)  # Field name made lowercase.
    cnn1_s_4 = models.FloatField(db_column='CNN1_s_4', blank=True, null=True)  # Field name made lowercase.
    cnn1_s_7 = models.FloatField(db_column='CNN1_s_7', blank=True, null=True)  # Field name made lowercase.
    cnn1_s_8 = models.FloatField(db_column='CNN1_s_8', blank=True, null=True)  # Field name made lowercase.
    cnn1_s_9 = models.FloatField(db_column='CNN1_s_9', blank=True, null=True)  # Field name made lowercase.
    cnn1_s_11 = models.FloatField(db_column='CNN1_s_11', blank=True, null=True)  # Field name made lowercase.
    cnn1_s_12 = models.FloatField(db_column='CNN1_s_12', blank=True, null=True)  # Field name made lowercase.
    cnn1_s_13 = models.FloatField(db_column='CNN1_s_13', blank=True, null=True)  # Field name made lowercase.
    cnn1_s_14 = models.FloatField(db_column='CNN1_s_14', blank=True, null=True)  # Field name made lowercase.
    cnn1_s_15 = models.FloatField(db_column='CNN1_s_15', blank=True, null=True)  # Field name made lowercase.
    cnn1_s_17 = models.FloatField(db_column='CNN1_s_17', blank=True, null=True)  # Field name made lowercase.
    cnn1_s_20 = models.FloatField(db_column='CNN1_s_20', blank=True, null=True)  # Field name made lowercase.
    cnn1_s_21 = models.FloatField(db_column='CNN1_s_21', blank=True, null=True)  # Field name made lowercase.
    cnn_s_2 = models.FloatField(db_column='CNN_s_2', blank=True, null=True)  # Field name made lowercase.
    cnn_s_3 = models.FloatField(db_column='CNN_s_3', blank=True, null=True)  # Field name made lowercase.
    cnn_s_4 = models.FloatField(db_column='CNN_s_4', blank=True, null=True)  # Field name made lowercase.
    cnn_s_7 = models.FloatField(db_column='CNN_s_7', blank=True, null=True)  # Field name made lowercase.
    cnn_s_8 = models.FloatField(db_column='CNN_s_8', blank=True, null=True)  # Field name made lowercase.
    cnn_s_9 = models.FloatField(db_column='CNN_s_9', blank=True, null=True)  # Field name made lowercase.
    cnn_s_11 = models.FloatField(db_column='CNN_s_11', blank=True, null=True)  # Field name made lowercase.
    cnn_s_12 = models.FloatField(db_column='CNN_s_12', blank=True, null=True)  # Field name made lowercase.
    cnn_s_13 = models.FloatField(db_column='CNN_s_13', blank=True, null=True)  # Field name made lowercase.
    cnn_s_14 = models.FloatField(db_column='CNN_s_14', blank=True, null=True)  # Field name made lowercase.
    cnn_s_15 = models.FloatField(db_column='CNN_s_15', blank=True, null=True)  # Field name made lowercase.
    cnn_s_17 = models.FloatField(db_column='CNN_s_17', blank=True, null=True)  # Field name made lowercase.
    cnn_s_20 = models.FloatField(db_column='CNN_s_20', blank=True, null=True)  # Field name made lowercase.
    cnn_s_21 = models.FloatField(db_column='CNN_s_21', blank=True, null=True)  # Field name made lowercase.
    lr_s_2 = models.FloatField(db_column='LR_s_2', blank=True, null=True)  # Field name made lowercase.
    lr_s_3 = models.FloatField(db_column='LR_s_3', blank=True, null=True)  # Field name made lowercase.
    lr_s_4 = models.FloatField(db_column='LR_s_4', blank=True, null=True)  # Field name made lowercase.
    lr_s_7 = models.FloatField(db_column='LR_s_7', blank=True, null=True)  # Field name made lowercase.
    lr_s_8 = models.FloatField(db_column='LR_s_8', blank=True, null=True)  # Field name made lowercase.
    lr_s_9 = models.FloatField(db_column='LR_s_9', blank=True, null=True)  # Field name made lowercase.
    lr_s_11 = models.FloatField(db_column='LR_s_11', blank=True, null=True)  # Field name made lowercase.
    lr_s_12 = models.FloatField(db_column='LR_s_12', blank=True, null=True)  # Field name made lowercase.
    lr_s_13 = models.FloatField(db_column='LR_s_13', blank=True, null=True)  # Field name made lowercase.
    lr_s_14 = models.FloatField(db_column='LR_s_14', blank=True, null=True)  # Field name made lowercase.
    lr_s_15 = models.FloatField(db_column='LR_s_15', blank=True, null=True)  # Field name made lowercase.
    lr_s_17 = models.FloatField(db_column='LR_s_17', blank=True, null=True)  # Field name made lowercase.
    lr_s_20 = models.FloatField(db_column='LR_s_20', blank=True, null=True)  # Field name made lowercase.
    lr_s_21 = models.FloatField(db_column='LR_s_21', blank=True, null=True)  # Field name made lowercase.
    lstm_s_2 = models.FloatField(db_column='LSTM_s_2', blank=True, null=True)  # Field name made lowercase.
    lstm_s_3 = models.FloatField(db_column='LSTM_s_3', blank=True, null=True)  # Field name made lowercase.
    lstm_s_4 = models.FloatField(db_column='LSTM_s_4', blank=True, null=True)  # Field name made lowercase.
    lstm_s_7 = models.FloatField(db_column='LSTM_s_7', blank=True, null=True)  # Field name made lowercase.
    lstm_s_8 = models.FloatField(db_column='LSTM_s_8', blank=True, null=True)  # Field name made lowercase.
    lstm_s_9 = models.FloatField(db_column='LSTM_s_9', blank=True, null=True)  # Field name made lowercase.
    lstm_s_11 = models.FloatField(db_column='LSTM_s_11', blank=True, null=True)  # Field name made lowercase.
    lstm_s_12 = models.FloatField(db_column='LSTM_s_12', blank=True, null=True)  # Field name made lowercase.
    lstm_s_13 = models.FloatField(db_column='LSTM_s_13', blank=True, null=True)  # Field name made lowercase.
    lstm_s_14 = models.FloatField(db_column='LSTM_s_14', blank=True, null=True)  # Field name made lowercase.
    lstm_s_15 = models.FloatField(db_column='LSTM_s_15', blank=True, null=True)  # Field name made lowercase.
    lstm_s_17 = models.FloatField(db_column='LSTM_s_17', blank=True, null=True)  # Field name made lowercase.
    lstm_s_20 = models.FloatField(db_column='LSTM_s_20', blank=True, null=True)  # Field name made lowercase.
    lstm_s_21 = models.FloatField(db_column='LSTM_s_21', blank=True, null=True)  # Field name made lowercase.
    mlp1_s_2 = models.FloatField(db_column='MLP1_s_2', blank=True, null=True)  # Field name made lowercase.
    mlp1_s_3 = models.FloatField(db_column='MLP1_s_3', blank=True, null=True)  # Field name made lowercase.
    mlp1_s_4 = models.FloatField(db_column='MLP1_s_4', blank=True, null=True)  # Field name made lowercase.
    mlp1_s_7 = models.FloatField(db_column='MLP1_s_7', blank=True, null=True)  # Field name made lowercase.
    mlp1_s_8 = models.FloatField(db_column='MLP1_s_8', blank=True, null=True)  # Field name made lowercase.
    mlp1_s_9 = models.FloatField(db_column='MLP1_s_9', blank=True, null=True)  # Field name made lowercase.
    mlp1_s_11 = models.FloatField(db_column='MLP1_s_11', blank=True, null=True)  # Field name made lowercase.
    mlp1_s_12 = models.FloatField(db_column='MLP1_s_12', blank=True, null=True)  # Field name made lowercase.
    mlp1_s_13 = models.FloatField(db_column='MLP1_s_13', blank=True, null=True)  # Field name made lowercase.
    mlp1_s_14 = models.FloatField(db_column='MLP1_s_14', blank=True, null=True)  # Field name made lowercase.
    mlp1_s_15 = models.FloatField(db_column='MLP1_s_15', blank=True, null=True)  # Field name made lowercase.
    mlp1_s_17 = models.FloatField(db_column='MLP1_s_17', blank=True, null=True)  # Field name made lowercase.
    mlp1_s_20 = models.FloatField(db_column='MLP1_s_20', blank=True, null=True)  # Field name made lowercase.
    mlp1_s_21 = models.FloatField(db_column='MLP1_s_21', blank=True, null=True)  # Field name made lowercase.
    rf_s_2 = models.FloatField(db_column='RF_s_2', blank=True, null=True)  # Field name made lowercase.
    rf_s_3 = models.FloatField(db_column='RF_s_3', blank=True, null=True)  # Field name made lowercase.
    rf_s_4 = models.FloatField(db_column='RF_s_4', blank=True, null=True)  # Field name made lowercase.
    rf_s_7 = models.FloatField(db_column='RF_s_7', blank=True, null=True)  # Field name made lowercase.
    rf_s_8 = models.FloatField(db_column='RF_s_8', blank=True, null=True)  # Field name made lowercase.
    rf_s_9 = models.FloatField(db_column='RF_s_9', blank=True, null=True)  # Field name made lowercase.
    rf_s_11 = models.FloatField(db_column='RF_s_11', blank=True, null=True)  # Field name made lowercase.
    rf_s_12 = models.FloatField(db_column='RF_s_12', blank=True, null=True)  # Field name made lowercase.
    rf_s_13 = models.FloatField(db_column='RF_s_13', blank=True, null=True)  # Field name made lowercase.
    rf_s_14 = models.FloatField(db_column='RF_s_14', blank=True, null=True)  # Field name made lowercase.
    rf_s_15 = models.FloatField(db_column='RF_s_15', blank=True, null=True)  # Field name made lowercase.
    rf_s_17 = models.FloatField(db_column='RF_s_17', blank=True, null=True)  # Field name made lowercase.
    rf_s_20 = models.FloatField(db_column='RF_s_20', blank=True, null=True)  # Field name made lowercase.
    rf_s_21 = models.FloatField(db_column='RF_s_21', blank=True, null=True)  # Field name made lowercase.
    rnn_s_2 = models.FloatField(db_column='RNN_s_2', blank=True, null=True)  # Field name made lowercase.
    rnn_s_3 = models.FloatField(db_column='RNN_s_3', blank=True, null=True)  # Field name made lowercase.
    rnn_s_4 = models.FloatField(db_column='RNN_s_4', blank=True, null=True)  # Field name made lowercase.
    rnn_s_7 = models.FloatField(db_column='RNN_s_7', blank=True, null=True)  # Field name made lowercase.
    rnn_s_8 = models.FloatField(db_column='RNN_s_8', blank=True, null=True)  # Field name made lowercase.
    rnn_s_9 = models.FloatField(db_column='RNN_s_9', blank=True, null=True)  # Field name made lowercase.
    rnn_s_11 = models.FloatField(db_column='RNN_s_11', blank=True, null=True)  # Field name made lowercase.
    rnn_s_12 = models.FloatField(db_column='RNN_s_12', blank=True, null=True)  # Field name made lowercase.
    rnn_s_13 = models.FloatField(db_column='RNN_s_13', blank=True, null=True)  # Field name made lowercase.
    rnn_s_14 = models.FloatField(db_column='RNN_s_14', blank=True, null=True)  # Field name made lowercase.
    rnn_s_15 = models.FloatField(db_column='RNN_s_15', blank=True, null=True)  # Field name made lowercase.
    rnn_s_17 = models.FloatField(db_column='RNN_s_17', blank=True, null=True)  # Field name made lowercase.
    rnn_s_20 = models.FloatField(db_column='RNN_s_20', blank=True, null=True)  # Field name made lowercase.
    rnn_s_21 = models.FloatField(db_column='RNN_s_21', blank=True, null=True)  # Field name made lowercase.
    svr_s_2 = models.FloatField(db_column='SVR_s_2', blank=True, null=True)  # Field name made lowercase.
    svr_s_3 = models.FloatField(db_column='SVR_s_3', blank=True, null=True)  # Field name made lowercase.
    svr_s_4 = models.FloatField(db_column='SVR_s_4', blank=True, null=True)  # Field name made lowercase.
    svr_s_7 = models.FloatField(db_column='SVR_s_7', blank=True, null=True)  # Field name made lowercase.
    svr_s_8 = models.FloatField(db_column='SVR_s_8', blank=True, null=True)  # Field name made lowercase.
    svr_s_9 = models.FloatField(db_column='SVR_s_9', blank=True, null=True)  # Field name made lowercase.
    svr_s_11 = models.FloatField(db_column='SVR_s_11', blank=True, null=True)  # Field name made lowercase.
    svr_s_12 = models.FloatField(db_column='SVR_s_12', blank=True, null=True)  # Field name made lowercase.
    svr_s_13 = models.FloatField(db_column='SVR_s_13', blank=True, null=True)  # Field name made lowercase.
    svr_s_14 = models.FloatField(db_column='SVR_s_14', blank=True, null=True)  # Field name made lowercase.
    svr_s_15 = models.FloatField(db_column='SVR_s_15', blank=True, null=True)  # Field name made lowercase.
    svr_s_17 = models.FloatField(db_column='SVR_s_17', blank=True, null=True)  # Field name made lowercase.
    svr_s_20 = models.FloatField(db_column='SVR_s_20', blank=True, null=True)  # Field name made lowercase.
    svr_s_21 = models.FloatField(db_column='SVR_s_21', blank=True, null=True)  # Field name made lowercase.
    xgb_s_2 = models.FloatField(db_column='XGB_s_2', blank=True, null=True)  # Field name made lowercase.
    xgb_s_3 = models.FloatField(db_column='XGB_s_3', blank=True, null=True)  # Field name made lowercase.
    xgb_s_4 = models.FloatField(db_column='XGB_s_4', blank=True, null=True)  # Field name made lowercase.
    xgb_s_7 = models.FloatField(db_column='XGB_s_7', blank=True, null=True)  # Field name made lowercase.
    xgb_s_8 = models.FloatField(db_column='XGB_s_8', blank=True, null=True)  # Field name made lowercase.
    xgb_s_9 = models.FloatField(db_column='XGB_s_9', blank=True, null=True)  # Field name made lowercase.
    xgb_s_11 = models.FloatField(db_column='XGB_s_11', blank=True, null=True)  # Field name made lowercase.
    xgb_s_12 = models.FloatField(db_column='XGB_s_12', blank=True, null=True)  # Field name made lowercase.
    xgb_s_13 = models.FloatField(db_column='XGB_s_13', blank=True, null=True)  # Field name made lowercase.
    xgb_s_14 = models.FloatField(db_column='XGB_s_14', blank=True, null=True)  # Field name made lowercase.
    xgb_s_15 = models.FloatField(db_column='XGB_s_15', blank=True, null=True)  # Field name made lowercase.
    xgb_s_17 = models.FloatField(db_column='XGB_s_17', blank=True, null=True)  # Field name made lowercase.
    xgb_s_20 = models.FloatField(db_column='XGB_s_20', blank=True, null=True)  # Field name made lowercase.
    xgb_s_21 = models.FloatField(db_column='XGB_s_21', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'shap_value'


class RulLoss(models.Model):
    id = models.BigIntegerField(primary_key=True)
    rul = models.BigIntegerField(db_column='RUL', blank=True, null=True)  # Field name made lowercase.
    rf_mean = models.FloatField(db_column='RF_mean', blank=True, null=True)  # Field name made lowercase.
    rf_std = models.FloatField(db_column='RF_std', blank=True, null=True)  # Field name made lowercase.
    rf_max = models.FloatField(db_column='RF_max', blank=True, null=True)  # Field name made lowercase.
    rf_min = models.FloatField(db_column='RF_min', blank=True, null=True)  # Field name made lowercase.
    svr_mean = models.FloatField(db_column='SVR_mean', blank=True, null=True)  # Field name made lowercase.
    svr_std = models.FloatField(db_column='SVR_std', blank=True, null=True)  # Field name made lowercase.
    svr_max = models.FloatField(db_column='SVR_max', blank=True, null=True)  # Field name made lowercase.
    svr_min = models.FloatField(db_column='SVR_min', blank=True, null=True)  # Field name made lowercase.
    xgb_mean = models.FloatField(db_column='XGB_mean', blank=True, null=True)  # Field name made lowercase.
    xgb_std = models.FloatField(db_column='XGB_std', blank=True, null=True)  # Field name made lowercase.
    xgb_max = models.FloatField(db_column='XGB_max', blank=True, null=True)  # Field name made lowercase.
    xgb_min = models.FloatField(db_column='XGB_min', blank=True, null=True)  # Field name made lowercase.
    lgb_mean = models.FloatField(db_column='LGB_mean', blank=True, null=True)  # Field name made lowercase.
    lgb_std = models.FloatField(db_column='LGB_std', blank=True, null=True)  # Field name made lowercase.
    lgb_max = models.FloatField(db_column='LGB_max', blank=True, null=True)  # Field name made lowercase.
    lgb_min = models.FloatField(db_column='LGB_min', blank=True, null=True)  # Field name made lowercase.
    bayes_mean = models.FloatField(db_column='BAYES_mean', blank=True, null=True)  # Field name made lowercase.
    bayes_std = models.FloatField(db_column='BAYES_std', blank=True, null=True)  # Field name made lowercase.
    bayes_max = models.BigIntegerField(db_column='BAYES_max', blank=True, null=True)  # Field name made lowercase.
    bayes_min = models.BigIntegerField(db_column='BAYES_min', blank=True, null=True)  # Field name made lowercase.
    rs_mean = models.FloatField(db_column='RS_mean', blank=True, null=True)  # Field name made lowercase.
    rs_std = models.FloatField(db_column='RS_std', blank=True, null=True)  # Field name made lowercase.
    rs_max = models.FloatField(db_column='RS_max', blank=True, null=True)  # Field name made lowercase.
    rs_min = models.FloatField(db_column='RS_min', blank=True, null=True)  # Field name made lowercase.
    lr_mean = models.FloatField(db_column='LR_mean', blank=True, null=True)  # Field name made lowercase.
    lr_std = models.FloatField(db_column='LR_std', blank=True, null=True)  # Field name made lowercase.
    lr_max = models.FloatField(db_column='LR_max', blank=True, null=True)  # Field name made lowercase.
    lr_min = models.FloatField(db_column='LR_min', blank=True, null=True)  # Field name made lowercase.
    mlp_mean = models.FloatField(db_column='MLP_mean', blank=True, null=True)  # Field name made lowercase.
    mlp_std = models.FloatField(db_column='MLP_std', blank=True, null=True)  # Field name made lowercase.
    mlp_max = models.FloatField(db_column='MLP_max', blank=True, null=True)  # Field name made lowercase.
    mlp_min = models.FloatField(db_column='MLP_min', blank=True, null=True)  # Field name made lowercase.
    mlp1_mean = models.FloatField(db_column='MLP1_mean', blank=True, null=True)  # Field name made lowercase.
    mlp1_std = models.FloatField(db_column='MLP1_std', blank=True, null=True)  # Field name made lowercase.
    mlp1_max = models.FloatField(db_column='MLP1_max', blank=True, null=True)  # Field name made lowercase.
    mlp1_min = models.FloatField(db_column='MLP1_min', blank=True, null=True)  # Field name made lowercase.
    lstm_mean = models.FloatField(db_column='LSTM_mean', blank=True, null=True)  # Field name made lowercase.
    lstm_std = models.FloatField(db_column='LSTM_std', blank=True, null=True)  # Field name made lowercase.
    lstm_max = models.FloatField(db_column='LSTM_max', blank=True, null=True)  # Field name made lowercase.
    lstm_min = models.FloatField(db_column='LSTM_min', blank=True, null=True)  # Field name made lowercase.
    cnn_mean = models.FloatField(db_column='CNN_mean', blank=True, null=True)  # Field name made lowercase.
    cnn_std = models.FloatField(db_column='CNN_std', blank=True, null=True)  # Field name made lowercase.
    cnn_max = models.FloatField(db_column='CNN_max', blank=True, null=True)  # Field name made lowercase.
    cnn_min = models.FloatField(db_column='CNN_min', blank=True, null=True)  # Field name made lowercase.
    cnn1_mean = models.FloatField(db_column='CNN1_mean', blank=True, null=True)  # Field name made lowercase.
    cnn1_std = models.FloatField(db_column='CNN1_std', blank=True, null=True)  # Field name made lowercase.
    cnn1_max = models.FloatField(db_column='CNN1_max', blank=True, null=True)  # Field name made lowercase.
    cnn1_min = models.FloatField(db_column='CNN1_min', blank=True, null=True)  # Field name made lowercase.
    gru_mean = models.FloatField(db_column='GRU_mean', blank=True, null=True)  # Field name made lowercase.
    gru_std = models.FloatField(db_column='GRU_std', blank=True, null=True)  # Field name made lowercase.
    gru_max = models.FloatField(db_column='GRU_max', blank=True, null=True)  # Field name made lowercase.
    gru_min = models.FloatField(db_column='GRU_min', blank=True, null=True)  # Field name made lowercase.
    lstm1_mean = models.FloatField(db_column='LSTM1_mean', blank=True, null=True)  # Field name made lowercase.
    lstm1_std = models.FloatField(db_column='LSTM1_std', blank=True, null=True)  # Field name made lowercase.
    lstm1_max = models.FloatField(db_column='LSTM1_max', blank=True, null=True)  # Field name made lowercase.
    lstm1_min = models.FloatField(db_column='LSTM1_min', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'rul_loss'


class InstanceHi(models.Model):
    input_id = models.BigIntegerField(primary_key=True)
    unit_number = models.FloatField(blank=True, null=True)
    hi_s_2 = models.FloatField(db_column='HI_s_2', blank=True, null=True)  # Field name made lowercase.
    hi_s_3 = models.FloatField(db_column='HI_s_3', blank=True, null=True)  # Field name made lowercase.
    hi_s_4 = models.FloatField(db_column='HI_s_4', blank=True, null=True)  # Field name made lowercase.
    hi_s_7 = models.FloatField(db_column='HI_s_7', blank=True, null=True)  # Field name made lowercase.
    hi_s_8 = models.FloatField(db_column='HI_s_8', blank=True, null=True)  # Field name made lowercase.
    hi_s_9 = models.FloatField(db_column='HI_s_9', blank=True, null=True)  # Field name made lowercase.
    hi_s_11 = models.FloatField(db_column='HI_s_11', blank=True, null=True)  # Field name made lowercase.
    hi_s_12 = models.FloatField(db_column='HI_s_12', blank=True, null=True)  # Field name made lowercase.
    hi_s_13 = models.FloatField(db_column='HI_s_13', blank=True, null=True)  # Field name made lowercase.
    hi_s_14 = models.FloatField(db_column='HI_s_14', blank=True, null=True)  # Field name made lowercase.
    hi_s_15 = models.FloatField(db_column='HI_s_15', blank=True, null=True)  # Field name made lowercase.
    hi_s_17 = models.FloatField(db_column='HI_s_17', blank=True, null=True)  # Field name made lowercase.
    hi_s_20 = models.FloatField(db_column='HI_s_20', blank=True, null=True)  # Field name made lowercase.
    hi_s_21 = models.FloatField(db_column='HI_s_21', blank=True, null=True)  # Field name made lowercase.
    hi = models.FloatField(db_column='HI', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'instance_hi'


class ModelScores(models.Model):
    id = models.BigIntegerField(primary_key=True)
    model = models.TextField(blank=True, null=True)
    score = models.FloatField(blank=True, null=True)
    rsme = models.FloatField(db_column='RSME', blank=True, null=True)  # Field name made lowercase.
    r2 = models.FloatField(db_column='R2', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'model_scores'
