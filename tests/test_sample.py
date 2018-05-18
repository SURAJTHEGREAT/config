import config_suraj.configuration as config
from oslo_config import cfg
def test_answer():

    filename='test.conf'
    db_opts = [
        cfg.BoolOpt('db_enable',default=False),
        cfg.StrOpt('host', default='mongo', help='host of db server'),
        cfg.IntOpt('port', default=27017, help='port of db server')
        ]

    tag='database'
    cfg.CONF=config.register_opts([filename],db_opts,tag)
    assert cfg.CONF.database.host=="mongodb"
    assert cfg.CONF.database.port==27017 

