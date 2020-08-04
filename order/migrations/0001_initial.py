# Generated by Django 3.0.8 on 2020-08-02 17:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Agent', models.CharField(max_length=20, unique=True)),
                ('Cash', models.IntegerField(default=0)),
                ('Wealth', models.IntegerField(default=0)),
                ('Email', models.CharField(default='', max_length=20)),
            ],
            options={
                'db_table': 'agents',
            },
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('Ticker', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('ClassName', models.CharField(max_length=100)),
                ('Department', models.CharField(max_length=50)),
                ('Shares', models.IntegerField()),
                ('ShortFee', models.FloatField(default=0.0)),
            ],
            options={
                'db_table': 'companies',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('OrderID', models.IntegerField(primary_key=True, serialize=False)),
                ('Type', models.CharField(choices=[('M', 'Market'), ('L', 'Limit')], max_length=1)),
                ('Direction', models.CharField(choices=[('A', 'Ask'), ('B', 'Bid')], max_length=20)),
                ('Price', models.IntegerField()),
                ('Quantity', models.IntegerField()),
                ('QuantityToFill', models.IntegerField()),
                ('Filled', models.CharField(default='N', max_length=1)),
                ('IDtoCancel', models.IntegerField()),
                ('Time', models.DateTimeField(auto_now_add=True)),
                ('Agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.Agent')),
                ('OrderBookName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.Company')),
            ],
            options={
                'db_table': 'orders',
            },
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('OrderBookName', models.CharField(max_length=20)),
                ('Price', models.IntegerField()),
                ('Quantity', models.IntegerField()),
                ('DirectionTrigger', models.CharField(max_length=1)),
                ('Asker', models.CharField(max_length=20)),
                ('Bidder', models.CharField(max_length=20)),
                ('BestAsk', models.IntegerField()),
                ('BestBid', models.IntegerField()),
                ('FillID', models.IntegerField(primary_key=True, serialize=False)),
                ('Time', models.DateTimeField(auto_now_add=True)),
                ('Asker_OrderID', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='Asker_OrderID', to='order.Order')),
                ('Bidder_OrderID', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='Bidder_OrderID', to='order.Order')),
            ],
            options={
                'db_table': 'prices',
            },
        ),
        migrations.CreateModel(
            name='AgentShare',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Shares', models.IntegerField(default=0)),
                ('Borrowed', models.IntegerField(default=0)),
                ('Collateral', models.IntegerField(default=0)),
                ('Agent', models.ForeignKey(db_column='agent_id', on_delete=django.db.models.deletion.CASCADE, to='order.Agent', to_field='Agent')),
                ('Company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.Company')),
            ],
            options={
                'db_table': 'agentshares',
                'unique_together': {('Agent_id', 'Company_id')},
            },
        ),
    ]